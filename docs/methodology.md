# Method

## Question and scope

I compare direct tram departures between three fixed city hubs in 2025. I ask how the service changes during the day, in the evening, by month and by day group. The hub names are listed in the README and in `HUBS` in `scripts/annual_stops.py`.

I include only trips with a tram mode code and ordinary boarding at the origin and alighting later at the destination. The destination does not need to be the end of the line. Both directions are counted separately. Circular lines can have different paths and journey lengths. I do not calculate the fastest route or journeys with a change.

## Timetable selection

`check_2025.py` reads the official rnv archive index. It checks snapshots published from December 2024 through December 2025. For each date, it selects the latest snapshot published before local midnight that contains active tram service. It combines `calendar.txt` with additions and removals in `calendar_dates.txt`.

This checks date coverage. It does not prove that every line or trip is present. The selected snapshot for each date is saved in `coverage_2025.json`.

## Hub matching

The script includes boarding platforms with the exact hub names. Some December feeds have blank stop names. A blank name is accepted only if the coordinates exactly match a hub position named in an earlier selected feed. I do not guess from nearby coordinates. This matching still needs a documented platform and line check.

## Time windows and excluded dates

- Daytime: 06:00 up to, but not including, 20:00.
- Evening: 22:00 up to, but not including, 02:00 the next day.
- GTFS times above 24:00 are moved to their calendar date. The calculation reads service dates on both sides of the year to complete the windows.
- All 12 public-holiday dates in the reference calendar are removed from the output. This is the same rule for every direction, even when a holiday applies in only one state.
- A non-holiday date is flagged `holiday_window_excluded` if the next date is a listed holiday. December 31 is also flagged because its evening enters January 1, 2026. There are 11 such dates per direction.
- Both windows are empty on a flagged date. I keep the same sample for the daytime and evening comparison, even though this removes some valid daytime data.
- March 29–30 and October 25–26 are flagged `clock_change_excluded`.
- Missing hub coverage is flagged `hub_missing`. No such rows appeared in the latest run.

The output has 353 rows per direction: 338 usable dates, 11 holiday-window exclusions and four clock-change exclusions. The holiday rule reduces uncertainty; it does not independently verify the remaining timetables. Other special timetables, such as Christmas Eve, still need a check.

## Metrics

I count departures within each window. Different trams at the same minute remain separate departures, including their zero-minute gap. For each date and window, I save the first and last departure, the median gap and the longest gap between departures.

Gap values need at least two departures. With zero or one departure the gap is empty, not zero. Gaps at the start and end of a window are not included. First and last values describe only the studied window, not the full service day.

Power Query adds month and day groups using the departure state's school calendar. DAX uses rows with `DataStatus = "ok"`. It calculates daily-count medians and medians of daily median gaps. Empty gaps do not contribute to gap medians. The daytime and evening windows last 14 and four hours, so their totals are not a direct frequency comparison.

`Flagged days` counts retained excluded rows. Public holidays have already been removed and are not part of this measure. Counts describe schedules, not actual operations or waiting times.

## Remaining validation

The Python run and output checks are recorded in [validation.md](validation.md). A sample still needs a comparison with independent, dated passenger timetables. Power Query and DAX have not been executed in Desktop. Replacement buses, accessibility, employment destinations and real-time data are future work.
