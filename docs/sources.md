# Source register

Updated: 13 November 2026. A page being available does not prove that a dataset is complete, downloaded or free to share.

## Historical rnv timetable check

The [official archive index](https://gtfs-sandbox-dds.rnv-online.de/) lists dated snapshots. The [publisher's catalogue description on GovData](https://www.govdata.de/suche/daten/soll-fahrplandaten-gtfs-general-transit-feed-specification?ids=0d16e520-d596-4c8f-9b0f-1a9331cd36c3) explains historical timestamp URLs and warns that some route records have no trips.

I downloaded 64 snapshots published from December 2024 through December 2025, including the preceding month for January coverage. All identify Rhein-Neckar-Verkehr GmbH (rnv) as the only agency. The observed mode codes are 0 (tram) and 3 (bus); the code also recognises extended tram codes. Every 2025 date has at least one active tram service in an already-published snapshot. This is date coverage, not proof of a complete network.

Download links are listed in the [official rnv archive](https://gtfs-sandbox-dds.rnv-online.de/). The script selects archives by publication date and checks their service calendars directly. Attribution: Rhein-Neckar-Verkehr GmbH (rnv). The archive is catalogued as dl-de/by-2-0; raw ZIP files are kept locally and are not shared here. Annual records keep quality flags. They describe scheduled service, not passenger demand or actual operation.

| Source | Intended role | Current status |
|---|---|---|
| [rnv network maps](https://www.rnv-online.de/fahrtinfo/liniennetzplaene/) | Rail scope, regular maps, night service and accessibility reference | Page inspected; full dataset inventory still needed |
| [VRN/RNN static GTFS catalogue](https://opendata.vrn.de/datasets/vrn-und-rnn-gtfs-sollfahrplandaten-aktuell) | Possible timetable source | Page inspected; its description excludes rail passenger timetable data and points to DELFI. Do not assume this feed covers rnv trams |
| [OpenData OePNV portal](https://www.opendata-oepnv.de/ht/de/datensaetze) | Possible rail-inclusive DELFI feed and operator datasets | Candidate only; endpoint, access, coverage and terms still need checking |
| [VRN open-data catalogue](https://opendata.vrn.de/dataset/search) | Search for real-time and stop-accessibility datasets | Coverage, identifiers and terms must be checked for each resource |
| [GTFS Schedule reference](https://gtfs.org/documentation/schedule/reference/) | Timetable parsing and calendar/time rules | Technical reference inspected |
| [GTFS Realtime reference](https://gtfs.org/documentation/realtime/reference/) | Future real-time work | Technical reference for later work |

## Accessibility and real-time data

| Source | What it provides | What this study can say |
|---|---|---|
| [rnv accessibility information](https://www.rnv-online.de/fahrtinfo/sicher-unterwegs/barrierefreiheit/) and the [stop plan for passengers with reduced mobility](https://www.rnv-online.de/media/rnv-online.de/Fahrtinfo/Liniennetzplaene/regulaer/Haltestellenplan_fuer_Mobilitaetseingeschraenkte.pdf) | Current stop and boarding information. The linked plan is valid from January 2026. | Useful for travel now, but not a historical record for 2025. Some coupled trams may not allow step-free boarding in the rear part at every stop. No 2025 accessibility score is made here. |
| [VRN/RNN GTFS Realtime dataset](https://opendata.vrn.de/datasets/vrn-und-rnn-gtfs-realtime-echtzeitfahrplandaten) and [VRN announcement](https://opendata.vrn.de/news/echtzeitfahrplandaten-ab-sofort-ueber-gtfs-realtime-verfuegbar) | Public bus and tram real-time data; the announcement dates availability from October 2025. The dataset description excludes rail passenger services (SPNV). | It can support a new collection from now on. I did not find a complete historical 2025 archive, so this study does not report yearly punctuality or cancellation rates. |
| [rnv Open Data](https://www.rnv-online.de/unternehmen/open-data/) | Information about the Start.Info API for current departures, disruption messages and route changes. | A possible source for future work. Access, terms, coverage and retention still need to be checked before collecting data. |

A real-time study should collect forecasts and observed outcomes over a defined period, match them to the planned trips, and report missing data. The current timetable files alone cannot show whether a tram actually ran on time.

## Before accepting a data source

Keep the publisher and link clear. Check that the timetable applies to the date and that its terms allow the planned use.

For rail timetables, check agency.txt, routes.txt and active trips against the official rnv network. Check interurban routes and replacement buses directly. Publish a coverage report before making network-wide comparisons.

For town boundaries, use a dated official source and check its licence before assigning stops to towns. For work destinations, record public addresses and explain how they were selected.

For real-time data, check access, licence, coverage, matching IDs and how long the data may be kept. No historical real-time feed or full record of actual arrivals is assumed.

## Current limits

Historical feeds have been downloaded and checked as described above. This project does not claim a complete, manually checked list of rnv rail lines, stops or towns. No historical real-time or passenger-load data have been acquired. Each new dataset needs its own source record and terms.

## Intercity comparison

The analysis compares direct tram trips between three fixed hubs, in six directions: Mannheim Hauptbahnhof, Ludwigshafen Berliner Platz (Bf LU Mitte), and Heidelberg Hauptbahnhof including Hauptbahnhof West. All platforms with these exact stop names are included; Hauptbahnhof Süd stops are outside these hub definitions.

A trip must allow normal boarding at the origin and normal alighting later at the destination on the same GTFS trip. All tram lines are eligible, and the destination need not be the final stop. This compares the selected hubs; it is not a measure of every trip between the towns. It does not find the fastest route or include changes.

Day groups use the calendar of the state where the trip starts. The windows are 06:00 to before 20:00 and 22:00 to 23:45 inclusive. Departures at 23:45 are included; later departures are not included in the evening count. Legal public holidays, clock-change dates and dates with missing hubs are not treated as normal usable days. Only records with status "ok" enter the report measures.

After the 12 public holidays are removed, there are 353 date records per direction, or 2,118 records in total. Four clock-change dates per direction are flagged. Missing hubs can add more flagged dates, so the number of usable dates differs by direction. In the current Mannheim-to-Heidelberg report view, 338 days are usable and 15 are flagged.

Different trips can leave in the same minute. They count as separate departures, and a zero-minute gap is kept. No matching direct tram trip was found between the selected Ludwigshafen and Heidelberg hubs in either direction in the studied windows. This is an archive finding for these hubs and time windows, not a claim about every stop or trips with a change.

Some December archive stop names are blank. These platforms are included only when their exact latitude and longitude match a hub platform named in an earlier selected archive. Renumbered IDs alone are not trusted. No nearest-stop guess is used.

## October construction check

The [rnv statement republished by MRN-News on 2 October 2025](https://www.mrn-news.de/2025/10/02/ludwigshafen-sperrungen-im-bereich-berliner-platz-und-wittelsbachplatz-604990/) reports closures at Berliner Platz and Wittelsbachplatz from 11 to 26 October. The notice links them to Hochstraße Süd construction and urgent track work. Lines 4/4A, 6/6A and 7 skip Berliner Platz; replacement buses are outside this tram-only analysis. [SWR reported the same works on 10 October 2025](https://www.swr.de/swraktuell/rheinland-pfalz/ludwigshafen/haltestelle-berliner-platz-und-rhein-haardtbahn-wegen-bauarbeiten-und-gleiserneuerung-gesperrt-100.html).

This fits the zero direct departures between the selected Mannheim and Ludwigshafen hubs from 11 to 24 October and the matching trips shown again on 27 October. The 25 and 26 October dates are flagged for the clock change. The timetable and notices give useful context, but they do not prove exactly what ran on every street.

## Public holidays in 2025

I checked the 12 legal holidays listed in [calendar_2025.md](calendar_2025.md): 1 January, 6 January, 18 April, 21 April, 1 May, 29 May, 9 June, 19 June, 3 October, 1 November, 25 December and 26 December. Epiphany on 6 January applies to Baden-Württemberg, not Rhineland-Palatinate; All Saints' Day on 1 November applies to both. The other dates apply in both states.

The selected GTFS snapshot for each date has no matching date-specific entry in calendar_dates.txt. The calculation would therefore use trips from the weekly service calendar. It can count a Thursday timetable on a Thursday holiday, for example, but cannot prove that rnv used that timetable on the holiday. All 12 public holidays are excluded from the daily analysis and Power Query results.

A useful example is 29 May (Ascension Day) and Sunday 1 June: both use snapshot 1747918025093. The feed gives 220 daytime Mannheim-to-Ludwigshafen departures for Thursday and 95 for Sunday. This shows that the file separates weekdays and Sundays. It does not prove that the Thursday holiday used the Thursday service.

For 1 January and 25–26 December, a [22 December 2024 report](https://www.mannheim24.de/mannheim/rnv-fahrplaene-heidelberg-mannheim-ludwigshafen-feiertage-weihnachten-silvester-zr-93482211.html) says Mannheim, Ludwigshafen and Heidelberg used the Sunday/public-holiday timetable. The current GTFS file gives 220 daytime Mannheim-to-Ludwigshafen trips for those dates. This is a count from the file, not confirmation of the actual holiday timetable.

For 6 January, 1 May and 29 May, I did not find a dated 2025 rnv notice or a public timetable in the sources checked. Counts from these files check the arithmetic only; they do not confirm the service used on the holiday.
