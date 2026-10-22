# rnv Tram Mobility Analysis

How does the rnv tram network connect everyday life across the Rhein-Neckar region?

This independent portfolio project currently compares direct rnv tram services between Mannheim, Ludwigshafen and Heidelberg, in both directions. It uses fixed hubs: Mannheim Hauptbahnhof, Ludwigshafen Berliner Platz (Bf LU Mitte), and Heidelberg Hauptbahnhof including Hauptbahnhof West. The five original research questions below remain the wider project context; accessibility and real-time reliability are not implemented.

**Study period: 1 January–31 December 2025.** The analysis uses 64 reviewed historical archives and produces 2,190 directional date records. Each direction has 361 usable dates and four clock-change exclusions. Dashboard files and narrative conclusions are still being reviewed locally and are not part of this release.

## Five research questions

| Theme | Question | Planned evidence |
|---|---|---|
| Evening service | Which corridors remain well connected after 22:00? | Scheduled departures, service spans and gaps by direction |
| Commuting | Which connections support early starts and late finishes? | Timetable-based journeys to documented employment destinations |
| Territory | How does service differ between central sections and outer branches? | Departures and headways by stop, corridor and municipality |
| Accessibility | Which stops have documented step-free access, and where is information missing? | Platform-level attributes and explicit unknown values |
| Reliability | How do real-time predictions differ from scheduled times? | A prospective collection, subject to feed coverage and terms |

## Scope and interpretation

Count tram trips that allow boarding at the origin hub and alighting later at the destination hub on the same trip. Include all platforms at the named hubs and all matching tram lines, in six directions. This compares these hubs, not every possible journey between the cities. No transfers or fastest-route calculation is included. Day groups use the departure state's calendar.

Exclude ordinary bus routes, S-Bahn, regional and long-distance rail from the core comparison. Record rail-replacement buses separately so construction does not appear as an unexplained loss of service. rnv is the operator; VRN is the wider transport association.

A tram-only analysis cannot establish total public-transport accessibility. Scheduled service is not observed operation. Real-time predictions alone do not prove actual punctuality or cancellations.

## Start here

- [Scope and analytical method](docs/methodology.md)
- [2025 holidays and school breaks](docs/calendar_2025.md)
- [Source register and unresolved coverage](docs/sources.md)
- [Delivery roadmap](docs/roadmap.md)
- [Data handling](data/README.md)

The reviewed 2025 calendar is supplied under `data/reference/`. Python prepares the timetable data; Power Query prepares the report table; DAX calculates the medians.

## Reproduce the analysis

Use Python 3.10 or later from the repository folder:

```text
python -m pip install -r requirements.txt
python scripts/check_2025.py
python scripts/annual_stops.py
python -m unittest discover -s scripts -p test_timetables.py
```

The first run downloads the 64 archives listed in `data/manifests/feeds_2025.json` (about 220 MB). Each file is checked against its recorded SHA-256. Archives stay in `data/raw/`; results are written to `data/processed/annual_stop_days.json`. Later runs reuse the local archives. The scripts use the standard library; Windows additionally needs the timezone database listed in `requirements.txt`.

For Power Query, create the `ProjectFolder` parameter using `powerbi/ProjectFolder.m` and replace the placeholder with this repository's full local folder path. Create a blank query named `ServiceDays` and paste `powerbi/ServiceDays.m` into its Advanced Editor. After loading it, create each measure in `powerbi/measures.dax` separately. The packaged Power BI dashboard is not published yet.

Daytime is 06:00–20:00; evening is 22:00–02:00 the next day. Use one direction at a time. Departure counts are daily medians; interval indicators are medians of daily median intervals, not measured passenger waiting times. A zero count describes the absence of matching direct trams in that window; it does not imply no public transport or no journey with a change.

## Next milestone

Complete the holiday-timetable spot-checks and verify data loading and visual layout in Power BI Desktop before publishing the dashboard. Finalise the README introduction and conclusions together.

Independent analysis, not an official rnv or VRN product. Source datasets retain their respective terms.
