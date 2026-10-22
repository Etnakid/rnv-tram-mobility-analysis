# Source register

Updated: 22 October 2026. Web-page availability does not establish dataset completeness, download success or permission to redistribute.

## Historical rnv timetable check

The [official archive index](https://gtfs-sandbox-dds.rnv-online.de/) lists dated snapshots. The [publisher's catalogue description on GovData](https://www.govdata.de/suche/daten/soll-fahrplandaten-gtfs-general-transit-feed-specification?ids=0d16e520-d596-4c8f-9b0f-1a9331cd36c3) explains historical timestamp URLs and warns that some route records have no trips.

Downloaded 64 snapshots published from December 2024 through December 2025, including the preceding month for January coverage. All identify Rhein-Neckar-Verkehr GmbH (rnv) as the sole agency. Observed mode codes are 0 (tram) and 3 (bus); the code also recognises extended tram codes. Every 2025 date has at least one active tram service in an already-published snapshot. This is date coverage, not proof of a complete network.

Download links are listed in the [official rnv archive](https://gtfs-sandbox-dds.rnv-online.de/). The script selects archives by publication date and checks their service calendars directly. Attribution: Rhein-Neckar-Verkehr GmbH (rnv). The archive is catalogued as dl-de/by-2-0; raw ZIPs are kept locally and not redistributed here. Annual records retain quality flags; they describe scheduled service, not passenger demand or observed operation.

| Source | Intended role | Current status |
|---|---|---|
| [rnv network maps](https://www.rnv-online.de/fahrtinfo/liniennetzplaene/) | Rail scope, regular/current maps, night service and accessibility reference | Page inspected; dataset inventory pending |
| [VRN/RNN static GTFS catalogue](https://opendata.vrn.de/datasets/vrn-und-rnn-gtfs-sollfahrplandaten-aktuell) | Candidate timetable source | Page inspected; its description excludes rail passenger timetable data and points to DELFI. Do not assume this feed covers rnv trams |
| [OpenData OePNV portal](https://www.opendata-oepnv.de/ht/de/datensaetze) | Candidate rail-inclusive DELFI feed and operator datasets | Candidate only; endpoint, access, coverage and terms pending |
| [VRN open-data catalogue](https://opendata.vrn.de/dataset/search) | Discovery of real-time and stop-accessibility datasets | Coverage, identifiers and terms must be checked per resource |
| [GTFS Schedule reference](https://gtfs.org/documentation/schedule/reference/) | Timetable parsing and calendar/time semantics | Technical reference inspected |
| [GTFS Realtime reference](https://gtfs.org/documentation/realtime/reference/) | Future real-time interpretation | Reference for later implementation |

## Before accepting a data source

Keep the publisher and source link clear, check timetable validity and terms, and distinguish access from permission to redistribute.

For rail timetables, inspect agency.txt, routes.txt and active trips and reconcile them with the official rnv network. Check interurban routes and replacement services explicitly. Publish a coverage report before using the feed for comparisons.

For municipal boundaries, identify a dated authoritative source and its licence before assigning stops to municipalities. For employment destinations, record public addresses and a transparent selection rule.

For real-time data, verify authentication, rate limits, rail coverage, static-feed compatibility and retention terms. No historical archive or complete observed-arrival record is assumed.

## Current limits

Historical feeds have been downloaded and inspected as described above. No complete, manually reconciled list of rnv rail lines, stops or municipalities is claimed. No historical real-time or occupancy data have been acquired. Additional datasets require their own provenance and terms.

## Intercity comparison

The analysis now counts direct tram trips between three fixed hubs, in both directions: Mannheim Hauptbahnhof, Ludwigshafen Berliner Platz (Bf LU Mitte), and Heidelberg Hauptbahnhof including Hauptbahnhof West. All boarding platforms with these exact stop names are included; Hauptbahnhof Süd stops are outside these hub definitions. A trip must allow ordinary boarding at the origin and ordinary alighting later at the destination on the same GTFS trip. All tram lines are eligible; the destination need not be the terminus. This is a hub comparison, not all journeys between municipal boundaries. Circular services can have different paths and journey lengths. No fastest-route or transfer calculation is claimed.

Day groups follow the departure state's calendar, including on cross-border journeys. The windows remain 06:00–20:00 and 22:00–02:00. Missing hubs and clock-change dates are excluded. Different trips departing in the same minute are valid separate departures; their zero-minute intervals are retained. A zero count means no matching direct tram departure during that window, not no transport between the cities. Medians can be zero even when occasional direct services exist. Earlier single-line terminal examples are superseded.

Some December archive stop names are blank. Those platforms are included only when their exact latitude/longitude matches a previously named hub platform from an earlier selected archive. Renumbered IDs alone are not trusted; no nearest-stop guess is used. All six directions have 361 usable dates and four clock-change exclusions. No matching direct departure was found for the Ludwigshafen–Heidelberg hub pair in either direction in the studied windows; this is an archive finding for these hubs, not a claim about every stop, every hour or transfer journeys.

## October construction cross-check

The [rnv statement republished by MRN-News on 2 October 2025](https://www.mrn-news.de/2025/10/02/ludwigshafen-sperrungen-im-bereich-berliner-platz-und-wittelsbachplatz-604990/) announces closures at Berliner Platz and Wittelsbachplatz from 11–26 October, linked to Hochstraße Süd construction and urgent track works. Lines 4/4A, 6/6A and 7 skip Berliner Platz; replacement buses are outside this tram-only analysis. The notice is corroborated by [SWR, 10 October 2025](https://www.swr.de/swraktuell/rheinland-pfalz/ludwigshafen/haltestelle-berliner-platz-und-rhein-haardtbahn-wegen-bauarbeiten-und-gleiserneuerung-gesperrt-100.html). This is consistent with zero direct departures in the selected hub pair on 11–24 October and resumed matching trips on 27 October. The intervening 25–26 October dates are clock-change exclusions, not evidence of resumed service. Holiday departure counts still require an external timetable check.
