# Delivery roadmap

## 0 — Project foundation (this release)

- [x] Agree on the rnv tram/interurban rail scope.
- [x] Preserve all five research questions.
- [x] Document method, source candidates and evidence limits.
- [ ] Acquire and verify transport data.

Progress on 22 October 2026: downloaded and inspected 64 historical feeds, found tram service on every 2025 date and ran a 10–16 March pilot. Historical line reconciliation and passenger-information spot-checks remain open, so the network verification milestone is not complete.

## 1 — Verified network inventory

- Select a rail-inclusive timetable snapshot and record provenance/terms.
- Publish the agency/route inclusion table and exclusions.
- Reconcile line coverage with official maps.
- Resolve boarding stops and municipal boundaries.
- Deliver reproducible ingestion and meaningful integrity checks.

Acceptance: another person can retrieve or obtain the documented input and reproduce the route/stop inventory. No unsupported total of cities or lines.

## 2 — Scheduled service

- Implement service calendars and cross-midnight timestamps.
- Analyse evening service and territorial differences.
- Add documented commuting scenarios.
- Publish metric definitions and spot-checks against timetables.

## 3 — Accessibility

- Assess platform-level coverage and source age.
- Publish accessible, inaccessible and unknown classifications separately.

## 4 — Real-time feasibility and collection

- Verify access, licence, coverage and static-trip matching.
- Specify observation period and sampling before collection.
- Separate prediction quality from measured operating punctuality.

If the feed is unsuitable, publish that limitation and retain the module as uncompleted.

## 5 — Presentation and independent reproduction

- Build a dashboard from validated outputs.
- Provide pinned dependencies, repeatable commands and a clean-environment check.
- Write neutral narrative conclusions supported by results.
- Ask an independent reviewer to reproduce the published release.

The comparison now covers three city pairs in both directions between fixed hubs. I count direct trams only, so trips with a change are outside this analysis. I removed all 12 legal holidays from the calculations. The result has 2,118 directional date records: 2,094 usable and 24 clock-change exclusions. I have not checked the Power BI query in Desktop yet, and this repository does not include a PBIX or PBIP report.
