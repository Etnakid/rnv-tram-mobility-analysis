# Delivery roadmap

## This release — scheduled trips between three hubs

- [x] Define the three hubs and the six directions.
- [x] Compare direct tram trips in the 2025 timetable archive.
- [x] Use clear day and evening windows, with holidays and flagged dates explained.
- [x] Check concrete examples against the archived timetable and construction notices.
- [x] Write down what the timetable can and cannot tell local passengers.
- [x] Check whether accessibility and real-time sources can support further conclusions.

The study is complete within this fixed scope. It is a comparison of planned direct tram trips between Mannheim Hauptbahnhof, Ludwigshafen Berliner Platz / Bf LU Mitte and Heidelberg Hauptbahnhof, including Hauptbahnhof West. It is not a complete inventory of every rnv line, and it does not include trips with a change.

The data contains 2,118 date-direction records after the 12 public holidays are removed. Clock-change dates and dates with missing hubs are flagged. Only records with status "ok" enter the report measures, so the number of usable dates differs by direction.

The timetable supports questions about service frequency, last departures and differences between weekdays and Sundays. It does not show passenger numbers or prove what ran on the street. The October construction example is supported by the timetable and public notices, but not by a record of actual tram movements.

## Separate work that needs new data

### Full network inventory

Use a rail-inclusive timetable source, list the included agencies and routes, and check its coverage against dated official maps. Publish the route and stop list before making network-wide claims.

### Accessibility by platform

Use dated platform-level information. Mark each platform as step-free, not step-free or unknown. The current rnv plan is useful for travel from 2026, but it does not establish conditions throughout 2025.

### Real-time reliability

Collect real-time forecasts and outcomes over a new, stated period. Check access, licence, route coverage, trip matching and missing records. Do not turn current feed availability into a claim about the full year 2025.

## Power BI report

The report file is kept outside this repository. Its page design now uses the navy-and-orange colour order and the tram artwork sits on the bottom edge. The annual evening cards still use the earlier 22:00–02:00 data import; refresh the model with the final 22:00–23:45 window before treating those annual values as final.
