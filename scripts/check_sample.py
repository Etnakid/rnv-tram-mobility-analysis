"""Compare four line 5 samples with the printed timetable linked in docs/sample_checks.md."""
import collections
import datetime as dt
import json
import zipfile
from check_2025 import RAW, OUT, TRAM_TYPES, active_services, read_table

SAMPLES = {
    '2025-03-12': ['10:13:00', '10:33:00', '10:53:00'],
    '2025-03-15': ['10:13:00', '10:33:00', '10:53:00'],
    '2025-03-16': ['10:24:00', '10:54:00'],
    '2025-04-15': ['10:13:00', '10:33:00', '10:53:00'],
}


def main():
    coverage = {r['date']: r['selected_snapshot']
                for r in json.loads((OUT / 'coverage_2025.json').read_text())}
    results = []
    for date, expected in SAMPLES.items():
        stamp = coverage[date]
        with zipfile.ZipFile(RAW / (stamp + '.zip')) as archive:
            stops = {r['stop_id']: r['stop_name'] for r in read_table(archive, 'stops.txt')}
            routes = {r['route_id'] for r in read_table(archive, 'routes.txt')
                      if r['route_short_name'] == '5' and r['route_type'] in TRAM_TYPES}
            active = active_services(read_table(archive, 'calendar.txt'),
                                     read_table(archive, 'calendar_dates.txt'),
                                     dt.date.fromisoformat(date))
            trips = {r['trip_id'] for r in read_table(archive, 'trips.txt')
                     if r['route_id'] in routes and r['service_id'] in active}
            times = read_table(archive, 'stop_times.txt')
        selected = {r['trip_id'] for r in times if r['trip_id'] in trips
                    and stops[r['stop_id']] == 'Leutershausen Bahnhof'
                    and r['departure_time'].startswith('10:')}
        by_trip = collections.defaultdict(list)
        for row in times:
            if row['trip_id'] in selected:
                by_trip[row['trip_id']].append(row)
        departures = []
        for trip_id, rows in by_trip.items():
            rows.sort(key=lambda row: int(row['stop_sequence']))
            for index, row in enumerate(rows):
                if stops[row['stop_id']] != 'Leutershausen Bahnhof':
                    continue
                later_names = [stops[r['stop_id']] for r in rows[index + 1:]]
                if not row['departure_time'].startswith('10:') or 'Schriesheim Bahnhof' not in later_names:
                    continue
                departures.append(dict(time=row['departure_time'], trip_id=trip_id,
                                       reaches_mannheim_hbf='MA Hauptbahnhof' in later_names,
                                       last_stop=stops[rows[-1]['stop_id']]))
        departures.sort(key=lambda row: row['time'])
        results.append(dict(date=date, snapshot=stamp, expected_times=expected,
                            times_match=[r['time'] for r in departures] == expected,
                            all_reach_mannheim_hbf=bool(departures) and
                            all(r['reaches_mannheim_hbf'] for r in departures),
                            departures=departures))
    (OUT / 'sample_checks.json').write_text(
        json.dumps(results, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for row in results:
        print(row['date'], '| times match:', row['times_match'],
              '| all reach Mannheim Hbf:', row['all_reach_mannheim_hbf'])


if __name__ == '__main__':
    main()
