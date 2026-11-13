# rnv Tram Mobility Analysis

How does the rnv tram network connect everyday life across the Rhein-Neckar region?

I usually get around by car, but every now and then I have taken the trams in this area. Those trips made me wonder how well Mannheim, Ludwigshafen and Heidelberg are connected, and what changes in the evening, at weekends and during school breaks.

This independent portfolio project currently compares direct rnv tram services between Mannheim, Ludwigshafen and Heidelberg, in both directions. It uses fixed hubs: Mannheim Hauptbahnhof, Ludwigshafen Berliner Platz (Bf LU Mitte), and Heidelberg Hauptbahnhof including Hauptbahnhof West. The five original research questions below remain the wider project context; accessibility and real-time reliability are not implemented.

**Study period: 1 January–31 December 2025.** The analysis uses 64 reviewed historical archives and produces 2,118 directional date records after excluding the 12 public holidays. Each direction has 349 usable dates; four clock-change dates are also excluded. I have not finished checking the Power BI report in Desktop, so I am leaving it out of this release.

## Five research questions

| Theme | Question | Planned evidence |
|---|---|---|
| Evening service | Which corridors remain well connected after 22:00? | Scheduled departures, service spans and gaps by direction |
| Commuting | Which connections support early starts and late finishes? | Timetable-based journeys to documented employment destinations |
| Territory | How does service differ between central sections and outer branches? | Departures and headways by stop, corridor and municipality |
| Accessibility | Which stops have documented step-free access, and where is information missing? | Platform-level attributes and explicit unknown values |
| Reliability | How do real-time predictions differ from scheduled times? | A prospective collection, subject to feed coverage and terms |

## Scope and interpretation

Count tram trips that allow boarding at the origin hub and alighting later at the destination hub on the same trip. Include all platforms at the named hubs and all matching tram lines, in six directions. This compares these hubs, not every possible journey between the cities. No transfers or fastest-route calculation is included. Public holidays remain in the reference calendar but are excluded from every service calculation because the historical holiday timetables could not be verified. Other day groups use the departure state's calendar.

Exclude ordinary bus routes, S-Bahn, regional and long-distance rail from the core comparison. Record rail-replacement buses separately so construction does not appear as an unexplained loss of service. rnv is the operator; VRN is the wider transport association.

A tram-only analysis cannot establish total public-transport accessibility. Scheduled service is not observed operation. Real-time predictions alone do not prove actual punctuality or cancellations.

## What I found

From Mannheim to Heidelberg, the median gap between direct tram departures rises from 10 minutes during the day (06:00–20:00) to 30 minutes in the evening (22:00–23:45). For Mannheim to Ludwigshafen, the median number of daytime departures is 125 on weekdays outside school breaks and 95 on Sundays.

Between 11 and 24 October, the timetable records no matching direct tram departures between the selected Mannheim and Ludwigshafen hubs in the studied windows. I found an rnv notice about construction around Berliner Platz and Wittelsbachplatz, with service changes from 11 to 26 October. This gives useful context for the gap, although the timetable alone cannot confirm what ran on the street ([rnv notice republished by MRN-News](https://www.mrn-news.de/2025/10/02/ludwigshafen-sperrungen-im-bereich-berliner-platz-und-wittelsbachplatz-604990/); [SWR report](https://www.swr.de/swraktuell/rheinland-pfalz/ludwigshafen/haltestelle-berliner-platz-und-rhein-haardtbahn-wegen-bauarbeiten-und-gleiserneuerung-gesperrt-100.html)).

For the selected hubs and time windows, the data contains no direct tram service between Ludwigshafen and Heidelberg. Since this analysis follows direct trams only, it does not describe journeys with a change.

I was sorry not to find suitable data on delays or passenger numbers. I had hoped to look at punctuality and crowding too, but the available sources did not give me enough evidence. Timetables show one part of a trip; the experience on board is another.

## Start here

- [Scope and analytical method](docs/methodology.md)
- [2025 holidays and school breaks](docs/calendar_2025.md)
- [Source register and unresolved coverage](docs/sources.md)
- [Delivery roadmap](docs/roadmap.md)
- [Data handling](data/README.md)

The reviewed 2025 calendar is supplied under `data/reference/`. Python leaves public-holiday dates out of the daily analysis file. Power Query joins the reference calendar and creates the remaining day groups; DAX calculates the medians.

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

Daytime is 06:00–20:00; evening is 22:00–23:45 inclusive. Use one direction at a time. Public holidays are excluded; departure counts are daily medians over the remaining dates. Interval indicators are medians of daily median intervals, not measured passenger waiting times. A zero count describes the absence of matching direct trams in that window; it does not imply no public transport or no journey with a change.

## Next milestone

Verify data loading and visual layout in Power BI Desktop before publishing the dashboard.

Independent analysis, not an official rnv or VRN product. Source datasets retain their respective terms.

