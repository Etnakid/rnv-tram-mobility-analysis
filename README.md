# rnv Direct Tram Connections — 2025

How do direct trams connect three city hubs during the day and in the evening?

I usually get around by car, but every now and then I have taken the trams in this area. Those trips made me wonder how well Mannheim, Ludwigshafen and Heidelberg are connected, and what changes in the evening, at weekends and during school breaks.

I compare tram departures between Mannheim, Ludwigshafen and Heidelberg in 2025, in both directions. Both hubs must appear in the same trip record in the data. I use three fixed hubs:

- Mannheim Hauptbahnhof.
- Ludwigshafen Berliner Platz (Bf LU Mitte).
- Heidelberg Hauptbahnhof, including Hauptbahnhof West.

I look at departures and gaps between trams by month and day group. This is a comparison of these hubs, not every possible journey between the cities.

## Current status

The Python calculation has been run again with 64 historical archives. It produces 2,118 direction/date records: 2,028 usable records and 90 flagged records. Each direction has 338 usable dates. See the [validation notes](docs/validation.md) for the checks and their limits.

A [small timetable sample](docs/sample_checks.md) matches departure times on four dates. It also shows an important limit: some line 5 trams can continue as line E under a new trip record. The current calculation does not join these records, so it can miss journeys where passengers stay on the tram. The figures are not the complete number of no-change connections.

Power Query and DAX files are included, but they still need a refresh and visual check in Power BI Desktop. This repository does not yet include a finished dashboard.

## Scope and exclusions

I count a trip when passengers can board at the origin hub and leave at the destination hub later on the same tram. All matching tram lines and platforms at the named hubs are included. Trips with a change, bus services, replacement buses, S-Bahn and regional trains are outside this calculation.

I remove all 12 public-holiday dates listed in the reference calendar. I also flag 11 other dates because their evening window enters a public holiday, including 31 December before New Year's Day. I leave both daytime and evening results empty on these dates, so both windows use the same dates. Four clock-change dates are also flagged. This leaves some valid daytime data unused, but keeps the comparison simple.

The same holiday exclusions apply to all directions. School-break groups use the departure state's calendar. Scheduled service does not show actual delays, cancellations or passenger numbers. Accessibility and the other original research ideas are [future work](docs/roadmap.md#future-work).

## What I found

From Mannheim to Heidelberg, the median gap between direct tram departures rises from 10 minutes during the day (06:00–20:00) to 30 minutes in the evening (22:00–02:00 the next day). For Mannheim to Ludwigshafen, the median number of daytime departures is 125 on weekdays outside school breaks and 95 on Sundays.

Between 11 and 24 October, the timetable records no matching direct tram departures between the selected Mannheim and Ludwigshafen hubs in the studied windows. I found an rnv notice about construction around Berliner Platz and Wittelsbachplatz, with service changes from 11 to 26 October. This gives useful context for the gap, although the timetable alone cannot confirm what ran on the street ([rnv notice republished by MRN-News](https://www.mrn-news.de/2025/10/02/ludwigshafen-sperrungen-im-bereich-berliner-platz-und-wittelsbachplatz-604990/); [SWR report](https://www.swr.de/swraktuell/rheinland-pfalz/ludwigshafen/haltestelle-berliner-platz-und-rhein-haardtbahn-wegen-bauarbeiten-und-gleiserneuerung-gesperrt-100.html)).

For the selected hubs and time windows, I found no single tram trip record containing both Ludwigshafen and Heidelberg hubs. This does not prove that every journey needs a change: linked trips and journeys with transfers are not included.

I was sorry not to find suitable data on delays or passenger numbers. I had hoped to look at punctuality and crowding too, but the available sources did not give me enough evidence. Timetables show one part of a trip; the experience on board is another.

## Start here

- [Scope and analytical method](docs/methodology.md)
- [2025 holidays and school breaks](docs/calendar_2025.md)
- [Source register and unresolved coverage](docs/sources.md)
- [Delivery roadmap](docs/roadmap.md)
- [Checks and remaining limits](docs/validation.md)
- [Passenger timetable samples and source checks](docs/sample_checks.md)
- [Power BI setup, one step at a time](powerbi/README.md)
- [Data handling](data/README.md)

The reviewed 2025 calendar is supplied under `data/reference/`. Python removes public-holiday rows and flags the other excluded dates. Power Query joins the reference calendar and creates the day groups; DAX calculates the medians from usable rows.

## Reproduce the analysis

Use Python 3.10 or later from the repository folder:

```text
python -m pip install -r requirements.txt
python scripts/check_2025.py
python scripts/annual_stops.py
```

The source is the [official rnv timetable archive](https://gtfs-sandbox-dds.rnv-online.de/). The first run downloads its historical ZIPs published from December 2024 through December 2025 (64 archives, about 220 MB, when this analysis was run). December 2024 is included because those timetables may still apply in early January. For each 2025 date, the script selects the latest already-published archive with valid tram service.

Archives stay in `data/raw/`; results are written to `data/processed/annual_stop_days.json`. Later runs reuse the local ZIPs. The scripts use the standard library; Windows additionally needs the timezone database listed in `requirements.txt`.

For Power Query, create the `ProjectFolder` parameter using `powerbi/ProjectFolder.m` and replace the placeholder with this repository's full local folder path. Create a blank query named `ServiceDays` and paste `powerbi/ServiceDays.m` into its Advanced Editor. After loading it, create each measure in `powerbi/measures.dax` separately. The packaged Power BI dashboard is not published yet.

Daytime is 06:00–20:00; evening is 22:00–02:00 the next day. These windows have different lengths, so their departure totals do not directly compare service frequency. Use one direction at a time.

Departure indicators are medians of daily counts. Gap indicators are medians of daily median gaps. They do not include the time from a window's start to the first tram, or from the last tram to its end. A day needs at least two departures to have a gap value. A blank gap is not zero and is left out of the gap median. These gaps are not measured passenger waiting times.

A zero departure count means no matching single-trip tram record was found in that window. It does not mean no public transport or no journey with a change. `Flagged days` counts retained rows with a quality flag; it does not include the 12 public-holiday dates removed before loading.

## Next milestone

Check a sample against dated passenger timetables, then verify data loading and visual layout in Power BI Desktop before publishing the dashboard.

Independent analysis, not an official rnv or VRN product. Source datasets retain their respective terms.

