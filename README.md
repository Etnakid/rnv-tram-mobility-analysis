# rnv Tram Mobility Analysis

How does the rnv tram network connect everyday life across the Rhein-Neckar region?

This independent portfolio project explores evening service, commuting connections, territorial differences, stop accessibility and service reliability. Its scope is the full rnv tram and interurban light-rail network, rather than a predetermined selection of cities.

**Status: project definition and source discovery. No transport dataset has been downloaded or analysed yet. No findings or dashboard are available in this first release.**

## Five research questions

| Theme | Question | Planned evidence |
|---|---|---|
| Evening service | Which corridors remain well connected after 22:00? | Scheduled departures, service spans and gaps by direction |
| Commuting | Which connections support early starts and late finishes? | Timetable-based journeys to documented employment destinations |
| Territory | How does service differ between central sections and outer branches? | Departures and headways by stop, corridor and municipality |
| Accessibility | Which stops have documented step-free access, and where is information missing? | Platform-level attributes and explicit unknown values |
| Reliability | How do real-time predictions differ from scheduled times? | A prospective collection, subject to feed coverage and terms |

## Scope and interpretation

Include urban tram and interurban rnv rail services after verifying their representation in the selected feed. Determine municipalities from validated stop coordinates and administrative boundaries. An authoritative route and municipality inventory is still pending.

Exclude ordinary bus routes, S-Bahn, regional and long-distance rail from the core comparison. Record rail-replacement buses separately so construction does not appear as an unexplained loss of service. rnv is the operator; VRN is the wider transport association.

A tram-only analysis cannot establish total public-transport accessibility. Scheduled service is not observed operation. Real-time predictions alone do not prove actual punctuality or cancellations.

## Start here

- [Scope and analytical method](docs/methodology.md)
- [Source register and unresolved coverage](docs/sources.md)
- [Delivery roadmap](docs/roadmap.md)
- [Data handling](data/README.md)

This release contains documentation only and requires no software installation. Planned tools are Python and SQL for preparation and analysis, followed by Power BI for presentation; dependencies and execution instructions will accompany working code.

## Next milestone

Acquire a suitable rail timetable snapshot, record its provenance and licence, and validate its rnv route/stop coverage against official maps before calculating indicators.

Independent analysis, not an official rnv or VRN product. Source datasets retain their respective terms.
