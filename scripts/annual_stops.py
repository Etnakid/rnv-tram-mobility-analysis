"""Count direct tram departures between three fixed city hubs in 2025."""
import collections
import datetime as dt
import json
import statistics
import zipfile
from check_2025 import RAW, OUT, TRAM_TYPES, YEAR_DAYS, active_services, read_table

HUBS = {
    'Mannheim': ['MA Hauptbahnhof'],
    'Ludwigshafen': ['Berliner Platz, Bf LU Mitte'],
    'Heidelberg': ['HD Hauptbahnhof', 'HD Hauptbahnhof West'],
}
STATES = {'Mannheim': 'BW', 'Ludwigshafen': 'RP', 'Heidelberg': 'BW'}
CONNECTIONS = [(a, b) for a in HUBS for b in HUBS if a != b]
DST_DATES = {'2025-03-29', '2025-03-30', '2025-10-25', '2025-10-26'}


def hub_stops(stops, positions=None):
    # Some archives omit names: reuse only exact positions already named in earlier feeds.
    if positions is None:
        positions = {}
    hubs = {}
    for row in stops:
        if row.get('location_type', '0') not in ('', '0'):
            continue
        position = (float(row['stop_lat']), float(row['stop_lon']))
        for city, names in HUBS.items():
            if row['stop_name'] in names:
                positions[position] = city
                hubs[row['stop_id']] = city
        if not row['stop_name'] and position in positions:
            hubs[row['stop_id']] = positions[position]
    return hubs


def direct_departures(rows, hubs):
    # A destination must appear later on the same trip; it need not be the terminus.
    for index, origin in enumerate(rows):
        city = hubs[origin['stop_id']]
        if origin.get('pickup_type', '0') not in ('', '0'):
            continue
        reached = set()
        for destination in rows[index + 1:]:
            target = hubs[destination['stop_id']]
            if target == city:
                break
            if target not in reached and destination.get('drop_off_type', '0') in ('', '0'):
                reached.add(target)
                yield city, target, origin


def load_connections(stamp, positions):
    with zipfile.ZipFile(RAW / (stamp + '.zip')) as archive:
        if 'frequencies.txt' in archive.namelist():
            raise ValueError('Frequency-based services require expansion')
        routes = {r['route_id']: r for r in read_table(archive, 'routes.txt')}
        trip_rows = [t for t in read_table(archive, 'trips.txt')
                     if routes[t['route_id']]['route_type'] in TRAM_TYPES]
        trips = {t['trip_id']: t for t in trip_rows}
        if len(trips) != len(trip_rows):
            raise ValueError('Duplicate trip IDs')
        hubs = hub_stops(read_table(archive, 'stops.txt'), positions)
        times = collections.defaultdict(list)
        for row in read_table(archive, 'stop_times.txt'):
            if row['trip_id'] in trips and row['stop_id'] in hubs:
                times[row['trip_id']].append(row)
        candidates = []
        for trip_id, rows in times.items():
            rows.sort(key=lambda row: int(row['stop_sequence']))
            if len({r['stop_sequence'] for r in rows}) != len(rows):
                raise ValueError('Duplicate hub stop sequence')
            values = [seconds(r['departure_time']) for r in rows]
            if values != sorted(values):
                raise ValueError('Hub times go backwards')
            trip = trips[trip_id]
            for origin, target, row in direct_departures(rows, hubs):
                candidates.append(dict(pair=(origin, target), service=trip['service_id'],
                                       departure=row['departure_time']))
        base = read_table(archive, 'calendar.txt')
        exceptions = read_table(archive, 'calendar_dates.txt')
        services = {r['service_id'] for r in base}
        services.update(r['service_id'] for r in exceptions if r['exception_type'] == '1')
        if any(t['service_id'] not in services for t in trips.values()):
            raise ValueError('Missing service calendar')
        return candidates, base, exceptions, set(hubs.values())


def seconds(value):
    hour, minute, second = map(int, value.split(':'))
    if hour < 0 or not 0 <= minute < 60 or not 0 <= second < 60:
        raise ValueError('Invalid GTFS time: ' + value)
    return hour * 3600 + minute * 60 + second


def window_stats(departures, start, end):
    selected = sorted(time for time in departures if start <= time < end)
    gaps = [(right - left).total_seconds() / 60 for left, right in zip(selected, selected[1:])]
    return {
        'departures': len(selected),
        'first': selected[0].isoformat() if selected else None,
        'last': selected[-1].isoformat() if selected else None,
        'median_gap_minutes': statistics.median(gaps) if gaps else None,
        'longest_gap_minutes': max(gaps) if gaps else None,
    }

def main():
    coverage = {r['date']: r['selected_snapshot']
                for r in json.loads((OUT / 'coverage_2025.json').read_text())}
    coverage['2024-12-31'] = coverage['2025-01-01']
    coverage['2026-01-01'] = coverage['2025-12-31']
    by_date = collections.defaultdict(list)
    present = {}
    positions = {}
    current_stamp = None
    # The extra service days complete the windows on either side of midnight.
    for day in [YEAR_DAYS[0] - dt.timedelta(days=1)] + YEAR_DAYS + [dt.date(2026, 1, 1)]:
        stamp = coverage[str(day)]
        if stamp != current_stamp:
            candidates, base, exceptions, cities = load_connections(stamp, positions)
            current_stamp = stamp
        active = active_services(base, exceptions, day)
        if not active:
            raise ValueError('No service calendar for ' + str(day))
        present[day] = cities
        for row in candidates:
            if row['service'] in active:
                # Times after 24:00 belong to the following calendar day.
                time = dt.datetime.combine(day, dt.time()) + dt.timedelta(seconds=seconds(row['departure']))
                by_date[(row['pair'], time.date())].append(time)
    results = []
    for origin, target in CONNECTIONS:
        pair = (origin, target)
        for day in YEAR_DAYS:
            tomorrow = day + dt.timedelta(days=1)
            midnight = dt.datetime.combine(day, dt.time())
            status = 'clock_change_excluded' if str(day) in DST_DATES else 'ok'
            if not {origin, target} <= present[day] & present[tomorrow]:
                status = 'hub_missing'
            values = by_date[(pair, day)] + by_date[(pair, tomorrow)]
            daytime = evening = None
            if status == 'ok':
                daytime = window_stats(values, midnight + dt.timedelta(hours=6), midnight + dt.timedelta(hours=20))
                evening = window_stats(values, midnight + dt.timedelta(hours=22), midnight + dt.timedelta(days=1, hours=2))
            results.append(dict(case=origin + ' → ' + target, date=str(day), state=STATES[origin],
                                status=status, daytime=daytime, evening=evening))
    assert len(results) == 2190
    assert len({(r['case'], r['date']) for r in results}) == 2190
    # Different trams may depart at the same minute; keep both departures.
    output = OUT / 'annual_stop_days.json'
    output.write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(dict(collections.Counter(r['status'] for r in results)))


if __name__ == '__main__':
    main()
