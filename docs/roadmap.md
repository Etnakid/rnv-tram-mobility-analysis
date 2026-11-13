# Delivery roadmap

## 0 — Project foundation (this release)

- [x] Agree on the rnv tram scope.
- [x] Keep all five research questions for the wider project.
- [x] Document the method, possible sources and evidence limits.
- [x] Download and inspect 64 historical feeds.
- [x] Compare direct tram trips between three fixed hubs, in both directions.
- [ ] Finish checking the full network and stop coverage.

Progress on 13 November 2026: the selected hubs and service windows are analysed. Every 2025 date has a published timetable snapshot with tram service. A full line-by-line network check and more spot-checks against passenger information are still open.

The daily file has 2,118 date-direction records after the 12 public holidays are removed. Dates with clock changes or missing hubs are flagged. Only records with status "ok" enter the report measures, so the number of usable dates can differ by direction. Trips with a change are outside this comparison.

## 1 — Verified network inventory

- Select a rail-inclusive timetable snapshot and record its source and terms.
- Publish the list of included agencies, routes and exclusions.
- Check line coverage against official maps.
- Check boarding stops and town boundaries.
- Provide steps that another person can repeat.

Acceptance: another person can obtain the documented input and reproduce the route and stop inventory. No unsupported total of towns or lines.

## 2 — Scheduled service

- Compare service calendars and times that pass midnight.
- Study evening service and differences between areas.
- Add clear examples for journeys to work.
- Define each measure and check examples against passenger timetables.

## 3 — Accessibility

- Check access at each platform and how old each source is.
- Show accessible, not accessible and unknown as separate results.

## 4 — Real-time service

- Check access, licence, coverage and trip matching.
- Choose the study period before collecting data.
- Separate forecast delays from measured delays.

If the feed is not suitable, report that limit and leave this part unfinished.

## 5 — Report and independent check

- Build a report from checked results.
- Provide clear versions of the tools and repeatable steps.
- Write conclusions that follow from the results.
- Ask another person to repeat the analysis.

The report file is kept outside this repository while its annual evening figures are refreshed for the final 22:00–23:45 window. This repository does not contain a PBIX or PBIP file.
