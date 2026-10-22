"""Download historical rnv timetables and select one for each 2025 day."""
import csv
import datetime as dt
import io
import json
from pathlib import Path
import urllib.request
import zipfile
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data/raw'
OUT = ROOT / 'data/processed'
ARCHIVE = 'https://gtfs-sandbox-dds.rnv-online.de/'
TRAM_TYPES = {'0', '900', '901', '902', '903', '904', '905', '906'}
WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
YEAR_DAYS = [dt.date(2025, 1, 1) + dt.timedelta(days=n) for n in range(365)]


def read_table(archive, name):
    if name not in archive.namelist():
        return []
    with archive.open(name) as file:
        return list(csv.DictReader(io.TextIOWrapper(file, encoding='utf-8-sig')))


def active_services(calendar, exceptions, day):
    date = day.strftime('%Y%m%d')
    active = set()
    for row in calendar:
        if row['start_date'] <= date <= row['end_date'] and row[WEEKDAYS[day.weekday()]] == '1':
            active.add(row['service_id'])
    # Special dates override the regular weekly timetable.
    for row in exceptions:
        if row['date'] != date:
            continue
        if row['exception_type'] == '1':
            active.add(row['service_id'])
        elif row['exception_type'] == '2':
            active.discard(row['service_id'])
        else:
            raise ValueError('Unknown calendar exception')
    return active


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(ARCHIVE, timeout=60) as response:
        index = json.load(response)
    feeds = []
    # December 2024 timetables may still be valid at the start of January.
    for item in sorted(index, key=lambda item: item['dir']):
        stamp = item['dir']
        if not stamp.isdigit():
            continue
        published = dt.datetime.fromtimestamp(int(stamp) / 1000, dt.timezone.utc).date()
        if not dt.date(2024, 12, 1) <= published <= dt.date(2025, 12, 31):
            continue
        path = RAW / (stamp + '.zip')
        if not path.exists():
            with urllib.request.urlopen(ARCHIVE + stamp + '/gtfs.zip', timeout=60) as response:
                data = response.read(50_000_001)
            if len(data) > 50_000_000:
                raise ValueError('Archive exceeds 50 MB')
            path.write_bytes(data)
        with zipfile.ZipFile(path) as archive:
            routes = {r['route_id'] for r in read_table(archive, 'routes.txt')
                      if r['route_type'] in TRAM_TYPES}
            services = {t['service_id'] for t in read_table(archive, 'trips.txt')
                        if t['route_id'] in routes}
            calendar = read_table(archive, 'calendar.txt')
            exceptions = read_table(archive, 'calendar_dates.txt')
            days = {str(day) for day in YEAR_DAYS
                    if active_services(calendar, exceptions, day) & services}
        feeds.append(dict(snapshot=stamp, days_with_tram_service=days))
    rows = []
    for day in YEAR_DAYS:
        midnight = dt.datetime.combine(day, dt.time(), ZoneInfo('Europe/Berlin'))
        available = [f for f in feeds if day.isoformat() in f['days_with_tram_service']]
        known = [f for f in available if int(f['snapshot']) <= midnight.timestamp() * 1000]
        if not known:
            raise ValueError('No previously published timetable for ' + str(day))
        chosen = max(known, key=lambda f: int(f['snapshot']))
        rows.append(dict(date=str(day), available_snapshots=len(available),
                         selected_snapshot=chosen['snapshot']))
    (OUT / 'coverage_2025.json').write_text(json.dumps(rows, indent=2) + '\n', encoding='utf-8')
    print('Archives checked:', len(feeds), '| Covered days:', len(rows))


if __name__ == '__main__':
    main()
