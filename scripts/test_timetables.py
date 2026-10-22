"""Small checks for the cases that can change the counts."""
import datetime as dt
import json
import unittest
from check_2025 import ROOT, active_services
from annual_stops import calendar_group, hub_stops, direct_departures, departure_datetime, window_stats

class TimetableChecks(unittest.TestCase):
    def test_all_named_hub_platforms_are_included_after_renumbering(self):
        rows = [dict(stop_id='new_A', stop_name='MA Hauptbahnhof', stop_lat='49.48', stop_lon='8.47'),
                dict(stop_id='new_B', stop_name='MA Hauptbahnhof', stop_lat='49.4801', stop_lon='8.47'),
                dict(stop_id='west', stop_name='HD Hauptbahnhof West', stop_lat='49.405', stop_lon='8.674'),
                dict(stop_id='other', stop_name='MA Hauptbahnhof Süd', stop_lat='49.477', stop_lon='8.467')]
        self.assertEqual(hub_stops(rows), {'new_A': 'Mannheim', 'new_B': 'Mannheim', 'west': 'Heidelberg'})

    def test_blank_names_require_an_exact_previously_named_position(self):
        positions = {}
        original = dict(stop_id='old', stop_name='MA Hauptbahnhof', stop_lat='49.48', stop_lon='8.47')
        hub_stops([original], positions)
        renamed = dict(original, stop_id='new', stop_name='')
        self.assertEqual(hub_stops([renamed], positions), {'new': 'Mannheim'})
        self.assertEqual(hub_stops([dict(renamed, stop_lat='49.49')], positions), {})

    def test_destination_is_later_on_the_same_trip_not_necessarily_the_terminus(self):
        hubs = {'a': 'Mannheim', 'b': 'Ludwigshafen', 'c': 'Heidelberg'}
        rows = [dict(stop_id=stop) for stop in ['a', 'b', 'c']]
        pairs = [(a, b) for a, b, row in direct_departures(rows, hubs)]
        self.assertEqual(pairs, [('Mannheim', 'Ludwigshafen'), ('Mannheim', 'Heidelberg'), ('Ludwigshafen', 'Heidelberg')])

    def test_two_platform_calls_at_one_hub_do_not_double_count_the_trip(self):
        hubs = {'a': 'Heidelberg', 'west': 'Heidelberg', 'b': 'Mannheim'}
        rows = [dict(stop_id=stop) for stop in ['a', 'west', 'b']]
        departures = list(direct_departures(rows, hubs))
        self.assertEqual(len(departures), 1)
        self.assertEqual(departures[0][2]['stop_id'], 'west')

    def test_boarding_and_alighting_must_be_allowed(self):
        hubs = {'a': 'Mannheim', 'b': 'Ludwigshafen'}
        for restriction in ['1', '2', '3']:
            rows = [dict(stop_id='a', pickup_type=restriction), dict(stop_id='b')]
            self.assertEqual(list(direct_departures(rows, hubs)), [])
            rows = [dict(stop_id='a'), dict(stop_id='b', drop_off_type=restriction)]
            self.assertEqual(list(direct_departures(rows, hubs)), [])

    def test_a_return_to_the_origin_is_not_an_extra_departure_to_the_next_city(self):
        hubs = {'a': 'Mannheim', 'b': 'Ludwigshafen', 'c': 'Heidelberg'}
        rows = [dict(stop_id=stop) for stop in ['a', 'b', 'a', 'c']]
        departures = list(direct_departures(rows, hubs))
        self.assertEqual(sum(a == 'Mannheim' and b == 'Heidelberg' for a, b, row in departures), 1)
        self.assertIs(departures[-1][2], rows[2])

    def test_public_holidays_and_weekends_are_not_mixed_with_school_weekdays(self):
        rows = json.loads((ROOT/'data/reference/calendar_2025.json').read_text(encoding='utf-8'))['days']
        calendar = {(r['date'],r['state']):r for r in rows}
        cases = [('2025-04-18','Public holiday'),('2025-04-19','Saturday'),('2025-04-14','Weekday, regional school break'),('2025-03-10','Weekday, outside regional school break')]
        for day,expected in cases:
            self.assertEqual(calendar_group(dt.date.fromisoformat(day),'BW',calendar),expected)

    def test_window_includes_midnight_without_crossing_the_end(self):
        start = dt.datetime(2025,3,10,22)
        end = dt.datetime(2025,3,11,2)
        departures = [start-dt.timedelta(minutes=1),start,start+dt.timedelta(minutes=20),start+dt.timedelta(minutes=50),end]
        result = window_stats(departures,start,end)
        self.assertEqual(result['departures'],3)
        self.assertEqual(result['median_gap_minutes'],25)
        self.assertEqual(result['longest_gap_minutes'],30)

    def test_no_gap_cannot_be_reported_as_zero(self):
        start = dt.datetime(2025,3,10,22)
        end = dt.datetime(2025,3,11,2)
        self.assertIsNone(window_stats([],start,end)['longest_gap_minutes'])
        self.assertIsNone(window_stats([start],start,end)['median_gap_minutes'])

    def test_calendar_exceptions_override_weekdays(self):
        base = dict(start_date='20250101',end_date='20251231',monday='1',tuesday='1',wednesday='1',thursday='1',friday='1',saturday='0',sunday='0',service_id='weekday')
        exceptions = [dict(service_id='weekday',date='20250310',exception_type='2'),dict(service_id='special',date='20250310',exception_type='1')]
        self.assertEqual(active_services([base],exceptions,dt.date(2025,3,10)),{'special'})
        self.assertEqual(active_services([base],exceptions,dt.date(2025,3,11)),{'weekday'})
        self.assertEqual(active_services([base],exceptions,dt.date(2025,3,16)),set())

    def test_calendar_boundaries_are_inclusive(self):
        base = dict(start_date='20250310',end_date='20250310',monday='1',service_id='one_day')
        self.assertEqual(active_services([base],[],dt.date(2025,3,10)),{'one_day'})
        self.assertEqual(active_services([base],[],dt.date(2025,3,17)),set())

    def test_after_midnight_uses_next_calendar_date(self):
        self.assertEqual(departure_datetime(dt.date(2025,3,9),'25:15:00'),dt.datetime(2025,3,10,1,15))
        self.assertEqual(departure_datetime(dt.date(2025,3,10),'00:05:00'),dt.datetime(2025,3,10,0,5))

if __name__=='__main__':
    unittest.main()
