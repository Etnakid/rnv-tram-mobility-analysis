# Scope and analytical method

Study period: 1 January–31 December 2025. Verify historical timetable coverage for every date before annual comparisons. See calendar_2025.md for state-level holidays and school breaks; local movable closures remain unknown. The reference calendar provides context and never overrides service calendars.

## Network boundary

The unit of scope is the rnv tram/interurban rail network, not an assumed list of cities. Build an explicit inclusion table containing source agency ID, route ID, public line name, mode, inclusion decision, rationale and snapshot date. Check urban and interurban rail encodings rather than assuming a single GTFS route_type captures the whole network.

Reconcile this table with the official rnv rail map and current service notices. Validate stops through trips and stop_times. Spatially join boarding-stop coordinates to dated municipal boundaries; inspect border cases and platforms manually. Publish exclusions and unmatched records. Do not infer the operator from a municipality or a line number alone.

Replacement buses belong in a separate disruption layer linked to their rail corridor. Keep regular-network maps separate from the service actually scheduled for the snapshot period.

## Calendar and time

Choose explicit dates only after inspecting feed validity. Compare ordinary weekdays, Saturdays and Sundays; identify public holidays and school-calendar effects. Resolve calendar.txt together with calendar_dates.txt.

Use the feed timezone and preserve GTFS times beyond 24:00:00. For an evening window of 22:00–02:00, include relevant services from both the current and previous service dates, convert them to dated local timestamps and deduplicate departures. Check daylight-saving transitions.

Calculate headways for each stop, direction and compatible destination pattern. Report edge gaps and first/last departures separately. A scheduled headway is not an observed passenger waiting time; 60 divided by hourly departures can hide uneven service.

## Five analysis modules

1. Evening: count boardable departures and measure service spans and gaps after 22:00; compare matched daytime windows.
2. Commuting: define public employment destinations and reproducible arrival/departure scenarios. Include walking, interchange rules and transfer time. Describe tram-only journeys and the limits of destination coverage.
3. Territory: compare stops and corridors within a documented geography. Avoid double-counting shared-track services or treating a municipality average as representative of every neighbourhood. Define central/outer categories before ranking results.
4. Accessibility: distinguish platform access, vehicle boarding and complete journey accessibility. Missing or unknown attributes remain unknown. Date-stamp evidence; do not equate an accessible station label with every platform being accessible.
5. Reliability: first establish real-time availability, matching keys and licence. Log observation time, feed timestamp, trip/stop identity and prediction horizon. Report collection gaps and stale records. Analyse prediction deviations unless actual arrival observations are demonstrably available. Missing updates alone do not establish cancellation.

## Validation before findings

Check primary and foreign keys, active service dates, monotonic stop sequences/times, valid coordinates, route coverage, pickup restrictions, duplicate snapshots and unknown accessibility values. If frequencies.txt is present, handle frequency-based service explicitly.

Manually reconcile selected stop/day timetables with official passenger information. Publish acquisition timestamps, source checksums, transformations, exclusions and denominators. Keep raw inputs immutable and generated outputs reproducible. No analytical validation has run in this documentation-only release.
