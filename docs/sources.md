# Source register

Discovery date: 20 October 2026. Web-page availability does not establish dataset completeness, download success or permission to redistribute.

| Source | Intended role | Current status |
|---|---|---|
| [rnv network maps](https://www.rnv-online.de/fahrtinfo/liniennetzplaene/) | Rail scope, regular/current maps, night service and accessibility reference | Page inspected; dataset inventory pending |
| [VRN/RNN static GTFS catalogue](https://opendata.vrn.de/datasets/vrn-und-rnn-gtfs-sollfahrplandaten-aktuell) | Candidate timetable source | Page inspected; its description excludes rail passenger timetable data and points to DELFI. Do not assume this feed covers rnv trams |
| [OpenData OePNV portal](https://www.opendata-oepnv.de/ht/de/datensaetze) | Candidate rail-inclusive DELFI feed and operator datasets | Candidate only; endpoint, access, coverage and terms pending |
| [VRN open-data catalogue](https://opendata.vrn.de/dataset/search) | Discovery of real-time and stop-accessibility datasets | Coverage, identifiers and terms must be checked per resource |
| [GTFS Schedule reference](https://gtfs.org/documentation/schedule/reference/) | Timetable parsing and calendar/time semantics | Technical reference inspected |
| [GTFS Realtime reference](https://gtfs.org/documentation/realtime/reference/) | Future real-time interpretation | Reference for later implementation |

## Before accepting a data source

Record exact download URL, publisher, retrieval time in UTC, SHA-256, feed validity, timezone, format, licence text/URL and required attribution. Keep the catalogue URL as well as the resource URL. Verify redistribution separately from access.

For rail timetables, inspect agency.txt, routes.txt and active trips and reconcile them with the official rnv network. Check interurban routes and replacement services explicitly. Publish a coverage report before using the feed for comparisons.

For municipal boundaries, identify a dated authoritative source and its licence before assigning stops to municipalities. For employment destinations, record public addresses and a transparent selection rule.

For real-time data, verify authentication, rate limits, rail coverage, static-feed compatibility and retention terms. No historical archive or complete observed-arrival record is assumed.

## Current limits

No feed has been selected or downloaded. No complete list of rnv rail lines, stops or municipalities is claimed. Dataset licences and attribution will be recorded resource by resource before ingestion or redistribution.
