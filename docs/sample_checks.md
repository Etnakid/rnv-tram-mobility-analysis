# Timetable sample checks

Checked on 12 November 2026. I used a separate passenger timetable as well as the GTFS archives. The results below are a small sample, not a check of every date or connection.

## 1. Line 5: four departure samples

I found a [VRN passenger timetable for Leutershausen Bahnhof](https://doko-sk95.de/wp-content/uploads/2025/01/RNV5_Richtung_Heidelberg_Mannheim_Viernheim.pdf), kept on a local club's website. It names rnv as the operator, is valid from December 15, 2024 and has a print date of January 29, 2025. This is a separate publication, not a second transport operator. I checked the actual PDF page, including the direction and destination notes.

PDF SHA-256: `ec05fb84eead50d726c90b3777e2d8e35e07dbdbeb25cec2401becf3447d7571`.

I selected the 10:00–11:00 hour toward Schriesheim and Heidelberg on a weekday, Saturday, Sunday and weekday during the BW school break. I compared all printed departures in that hour with active line 5 trips at the same stop in the selected GTFS archive.

| Date | Day group | Printed departures | GTFS departures | Snapshot | Result |
|---|---|---|---|---|---|
| 2025-03-12 | Weekday outside regional break | 10:13, 10:33, 10:53 | 10:13, 10:33, 10:53 | 1741268517582 | Times match |
| 2025-03-15 | Saturday | 10:13, 10:33, 10:53 | 10:13, 10:33, 10:53 | 1741268517582 | Times match |
| 2025-03-16 | Sunday | 10:24, 10:54 | 10:24, 10:54 | 1741268517582 | Times match; destination differs |
| 2025-04-15 | Weekday in regional break | 10:13, 10:33, 10:53 | 10:13, 10:33, 10:53 | 1744286404699 | Times match |

### Destination difference on Sunday

The printed Sunday trips have a note giving Mannheim Hauptbahnhof as the destination. The GTFS trips `5-22-5-36780` and `5-22-5-38580` end at Paradeplatz and contain no `MA Hauptbahnhof` stop. The production script therefore does not count them as direct Heidelberg–Mannheim hub trips.

I have not resolved this difference. A later timetable change, a feed problem or another explanation is possible; the sample does not establish which. I have not added trips or changed the counting rule to make the figures agree.

For the other three dates, the sampled GTFS trips contain both HD Hauptbahnhof and MA Hauptbahnhof later in their stop sequence. This checks the encoded path, not actual operation. The source does not give a separate exact validity-end date, so later changes cannot be ruled out.

Leutershausen is outside the three study hubs. These checks support the departure-time and calendar calculation on one line. They do not independently verify the daily hub totals or every platform.

### Repeat the sample

After running the two main scripts:

```text
python scripts/check_sample.py
```

The script writes `data/processed/sample_checks.json`, including snapshot IDs, trip IDs, departure times, final stops and whether MA Hauptbahnhof appears later. The expected times were read manually from the linked PDF; the script does not download or parse it. Inspect the linked page again if its contents change.

## 2. October works: an official city notice

The [City of Ludwigshafen notice, published October 24, 2025](https://ludwigshafen-diskutiert.de/node/1056), says that trams and buses return to Berliner Platz on October 27 after works from October 11 to 26. The site's [legal notice](https://ludwigshafen-diskutiert.de/impressum) identifies the city as responsible for its content.

| Sample date | Mannheim to Ludwigshafen: daytime / evening | Return direction: daytime / evening | Interpretation |
|---|---|---|---|
| 2025-10-15 | 0 / 0 | 0 / 0 | Consistent with the works notice |
| 2025-10-27 | 125 / 14 | 125 / 13 | Direct trips appear after the announced return |

The city notice supports the timing of the works. It does not confirm the exact departure counts or show what actually ran. Replacement buses remain outside the calculation.

## 3. Hub records in selected archives

I inspected five selected snapshots using the production hub-matching rule. The counts below are matched boarding-stop records, not a verified number of physical tram platforms. They can include stop records that do not have tram trips.

| Sample date | Snapshot | Mannheim records | Ludwigshafen records | Heidelberg records |
|---|---|---|---|---|
| 2025-03-12 | 1741268517582 | 5 | 6 | 9 |
| 2025-04-15 | 1744286404699 | 5 | 6 | 9 |
| 2025-10-15 | 1760008182193 | 4 | 2 | 8 |
| 2025-10-27 | 1761228820050 | 4 | 6 | 8 |
| 2025-12-21 | 1765456014860 | 4 | 6 | 8 |

No blank-name fallback was used for the matched records in these five snapshots. During the works, the October 15 archive still has two matching Ludwigshafen stop records, but no tram stop-time rows at them. A stop record alone does not prove that trams serve it.

I also found a [preserved rnv line 21 timetable, valid from June 23, 2025](https://www.nahverkehr-rheinneckar.de/.cm4all/mediadb/dateien/dokumente/fahrplaene/hd/linie21_20250623.pdf). It names HD Hauptbahnhof on the route, consistent with line 21 records in the sampled feeds. This is a stop/line-name check only. Physical platform matching and a complete line inventory remain open.

## 4. Sources not accepted as dated 2025 checks

- The rnv [Schriesheim line 5 poster](https://www.rnv-online.de/media/rnv-online.de/Fahrtinfo/Fahrplaene/Aushangfahrplaene_2020/01005P_2_03479_1.pdf) was indexed with a 2025 validity date. The downloaded page now says September 14, 2026. I did not use it to verify 2025 times.
- The [Seckenheim line 5 poster](https://www.rnv-online.de/media/rnv-online.de/Fahrtinfo/Fahrplaene/Aushangfahrplaene_2020/01005P_2_02594_21.pdf) was also indexed as a 2025 source. The downloaded page now says September 14, 2026. It was not used in the accepted samples.
- A [VRN brochure with 2025 in the filename](https://www.vrn.de/mam/service/downloads/linienbuendel/dokumente/2025-fpb_leimen_sandhausen_st_leon_rot_bf.pdf) has PDF modification metadata from February 2026. I did not treat it as a dated 2025 version of the exact timetable.

A search result or filename is not enough to establish historical validity.
