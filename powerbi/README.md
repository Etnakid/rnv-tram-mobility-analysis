# Power BI report

I include a draft report in `RNV_Mobility_2025.pbix`. It has two pages: Service overview and Coverage and notes. It opened in Power BI Desktop on 12 November 2026. The screenshot shows the expected Mannheim to Heidelberg values. Other directions, filter changes and a fresh reload still need review.

The report uses orange and blue, simple cards and a tram illustration. I am improving the text size, filters and background after the first Desktop review.

To use the snapshot, open the PBIX file. To refresh it, first create the data below, then set the `ProjectFolder` parameter to your local repository folder. The embedded snapshot keeps the data available before refresh.

The steps below explain how I can rebuild the report from the data. The draft visuals use simple median and count aggregations; `measures.dax` is a separate reference and is not loaded in the PBIX. Keep one direction selected.

## 1. Create the data

From the repository folder, run these commands one at a time:

```text
python -m pip install -r requirements.txt
python scripts/check_2025.py
python scripts/annual_stops.py
```

Check that `data/processed/annual_stop_days.json` exists. Keep the repository in the same folder while building the report.

## 2. Set the folder

Open a new report in Power BI Desktop. Open Power Query and create a blank query named `ProjectFolder`.

Open its Advanced Editor. Paste the contents of `ProjectFolder.m`. Replace `__SET_PROJECT_FOLDER__` with the full Windows path to this repository, for example `C:\Users\YourName\Documents\rnv-project`.

## 3. Load the results

Create another blank query named `ServiceDays`. In its Advanced Editor, paste `ServiceDays.m`.

Apply the changes. The table should have 2,118 rows. If there is an error, check the folder path and that both JSON files exist: the generated results and `data/reference/calendar_2025.json`.

## 4. Create the measures

Select the `ServiceDays` table and create a new measure. Paste one measure at a time from `measures.dax`, including its name and formula. Do not paste the whole file into one measure.

If updating an older report, rename `Excluded days` to `Flagged days` and check any visuals using it. The 12 public-holiday dates were removed before loading, so they are not in this measure.

## 5. Add two filters

Add a Connection slicer and turn on single selection. Add a Month slicer.

Keep one direction selected. For monthly charts, use the `Month` date itself, not a year/quarter/day hierarchy. Sort `DayGroup` by `DayGroupOrder` to keep the weekday and weekend groups in the intended order.

## 6. Build one page

Use a dark blue background, orange as the main accent and blue for the evening trend. Keep the labels short. The initial layout is:

| Part | Visual | Fields or measures |
|---|---|---|
| Top | Title and filters | Connection and Month |
| First row | Four cards | Median daytime departures; Median evening departures; Eligible days; Flagged days |
| Middle left | Column chart | DayGroup; Median daytime departures |
| Middle right | Line chart | Month; Median evening departures |
| Bottom | Small table | Median daily daytime gap; Days with daytime gap; Median daily evening gap; Days with evening gap |

Use these card labels: `Day departures (06–20)` and `Evening departures (22–02)`. Counts are daily medians, not totals for the selection. The windows last 14 and four hours, so their counts do not directly compare frequency.

Keep this note visible on the page:

> Only trips with both hubs in one trip record are counted. Some trams continue under a new trip record and are missing from this count. These are planned departures, not actual arrivals.

The gap table shows how many days have enough departures for a gap value. Blank gaps are not zero. Add `Connection summary` in a separate text/card visual only if it remains easy to read.

## 7. Check the numbers

Clear Month and DayGroup filters. Select one direction at a time. These are Python reference values for the current branch; they are not proof of complete transport coverage.

| Direction | Day departures | Evening departures | Day gap / days used | Evening gap / days used |
|---|---|---|---|---|
| Mannheim to Heidelberg | 77 | 4 | 10 min / 337 | 30 min / 332 |
| Heidelberg to Mannheim | 63 | 3 | 10 min / 330 | 30 min / 332 |
| Mannheim to Ludwigshafen | 125 | 14 | 8 min / 324 | 15 min / 324 |
| Ludwigshafen to Heidelberg | 0 | 0 | Blank / 0 | Blank / 0 |

Each selected direction should show 338 eligible days and 15 flagged days. Changing Month or DayGroup should update the numbers. Clearing Connection should leave numeric measures blank and show a prompt in `Connection summary`.

Do not turn blank gaps into zero. Do not apply an `ok` filter to the whole page: it would hide flagged dates from the quality count. The measures already select usable rows where needed.

## 8. Save the draft

Save a local PBIX file. Refresh it once more and check the filters and notes. Do not call it a finished report until Desktop checks pass. This named draft PBIX is tracked in Git. Other local PBIX files remain ignored.

Helpful Microsoft guides: [create measures](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-tutorial-create-measures) and [sort one column by another](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-sort-by-column).
