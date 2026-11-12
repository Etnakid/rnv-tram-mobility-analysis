# Roadmap

## First version: direct tram connections in 2025

I want to finish a small study that another person can understand and run. The first version compares direct trams between the three hubs. It does not need every original research idea to be complete.

### 1. Scope and calendar rules

- [x] Define the hubs, six directions and two time windows.
- [x] Download historical feeds and calculate the daily results.
- [x] Remove public holidays and flag evenings that enter a holiday.
- [x] Use the same dates for the daytime and evening comparison.
- [x] Explain zero values, empty gaps and excluded dates.

### 2. Check the evidence

- [x] Run the Python calculation again and check its output.
- [ ] Check the hub platforms and matching tram lines in selected feeds.
- [ ] Compare a weekday, Saturday, Sunday and school-break date with dated passenger timetables.
- [ ] Include an October construction date in the checks.
- [ ] Record the source, expected value, calculated value and any difference.

Done when the sample checks are documented and any unresolved differences are clear. Repeating the GTFS calculation alone is not an independent timetable check.

### 3. Finish Power BI

- [ ] Refresh `ServiceDays` in Power BI Desktop.
- [ ] Check every measure against the Python output.
- [ ] Check one-direction filters, empty results and excluded dates.
- [ ] Build one or two pages with counts, gaps, monthly changes and clear notes.
- [ ] Keep the number of days used for gap values visible.

Done when refresh, filters and visuals have been checked in Desktop. The M and DAX files alone are not a finished dashboard.

### 4. Publish the portfolio version

- [ ] Include a report file or download link and dashboard screenshots.
- [ ] Publish a small results table after checking the source terms.
- [ ] Write three findings with their limits in simple English.
- [ ] Ask another person to follow the setup instructions.

Done when a reader can inspect the results without downloading all the raw feeds and can also reproduce the calculation.

## Future work

These were the wider questions behind the project. They are not implemented in the first version.

| Topic | Possible next step |
|---|---|
| Evening service | Compare more stops and include gaps at window boundaries |
| Commuting | Define work destinations and journeys with transfers |
| Territory | Compare central sections and outer branches using documented areas |
| Accessibility | Check platform-level sources and keep unknown values separate |
| Reliability | Check real-time access and terms before collecting new observations |

Replacement-bus data could also help explain construction periods. The current tram calculation does not count these buses.
