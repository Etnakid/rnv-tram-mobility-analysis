# Validation notes

Checked on 12 November 2026 with Python 3.12.14 on Linux.

## What I ran

The baseline was commit `e78eb9111cd2c907a02e1997c4e82babf0c18b75`. The first run downloaded and checked 64 archives and produced coverage for all 365 dates. The revised calculation reused those archives and the same `coverage_2025.json`.

To run the calculation from the repository folder:

```text
python -m pip install -r requirements.txt
python scripts/check_2025.py
python scripts/annual_stops.py
```

## Output checks

| Check | Result |
|---|---|
| Direction/date rows | 2,118 |
| Unique direction/date keys | 2,118 |
| Usable rows | 2,028: 338 per direction |
| Holiday-window flags | 66: 11 per direction |
| Clock-change flags | 24: four per direction |
| Missing-hub flags | None in this run |
| Public-holiday rows | None: all 12 dates were removed |
| Change from the baseline output | Exactly 66 rows changed; every other row was identical |

The 66 changed rows now have `status = "holiday_window_excluded"` and empty daytime and evening values. Empty values are not zero departures.

The excluded evening dates are January 5, April 17, April 20, April 30, May 28, June 8, June 18, October 2, October 31, December 24 and December 31. The last date enters January 1, 2026, outside the daily reference calendar.

## Findings checked again

- Mannheim to Heidelberg: the median of daily median gaps remains 10 minutes in daytime and 30 minutes in the evening.
- Mannheim to Ludwigshafen: median daytime departures remain 125 on weekdays outside regional school breaks and 95 on Sundays.
- Mannheim to Ludwigshafen, and back: all 14 dates from October 11 to 24 still have zero matching departures in both windows.
- Ludwigshafen to Heidelberg, and back: all usable dates have zero matching direct departures in both windows.

These checks use the generated JSON. The day groups were checked in Python using the reference calendar. They do not prove that the Power Query and DAX implementation runs correctly in Desktop.

## Passenger timetable and hub samples

The [sample checks](sample_checks.md) compare 11 departures on four dates with a separate printed timetable. All departure times match. For two Sunday trips, an official rnv article and same-stop/time E trips support a line-change explanation. The archive lacks vehicle links, so the annual calculation does not join them. This is a known coverage limit, not a full pass for all no-change journeys. Five selected archives were also checked for matching hub records. An official city notice supports the October construction dates.

Repeat the departure sample after the main calculation with `python scripts/check_sample.py`. The expected times were read manually from the printed source.

## What is still unverified

- The sample checks do not independently verify complete daily hub totals. Possible line 5 to E continuations are not included in the annual totals.
- Hub stop records were inspected in five snapshots, but physical platforms and full line coverage have not been verified.
- The holiday exclusions reduce uncertainty. They do not verify every remaining special timetable, such as Christmas Eve daytime service.
- Power Query refresh, DAX measures and visual layout have not been tested in Power BI Desktop.
- Windows setup has not been tested in this run.
- No actual operations, delays, passenger counts or replacement-bus services were validated.

For an existing local Power BI report, rename the old `Excluded days` measure to `Flagged days` and check any visuals that use it. The repository does not include a packaged report to update automatically.

## Power BI preparation

The [Desktop guide](../powerbi/README.md) gives one page to build and reference values to check. Two small DAX measures count the days used for daytime and evening gaps. Their expected counts were calculated in Python, but the DAX formulas and report still need to run in Desktop. No PBIX report or successful Desktop refresh is claimed.
