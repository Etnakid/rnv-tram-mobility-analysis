let
    Folder = Text.TrimEnd(ProjectFolder, {"\", "/"}),

    // Read the daily results and keep the fields used in the report.
    Source = Json.Document(File.Contents(Folder & "\data\processed\annual_stop_days.json")),
    Raw = Table.FromRecords(Source),
    Selected = Table.SelectColumns(Raw, {"case", "date", "state", "status", "daytime", "evening"}),
    Renamed =
        Table.RenameColumns(
            Selected,
            {{"case", "Connection"}, {"date", "Date"}, {"state", "State"}, {"status", "DataStatus"}}
        ),
    TypedKeys =
        Table.TransformColumnTypes(
            Renamed,
            {
                {"Connection", type text},
                {"Date", type date},
                {"State", type text},
                {"DataStatus", type text}
            },
            "en-US"
        ),
    CleanText =
        Table.TransformColumns(
            TypedKeys,
            {
                {"Connection", Text.Trim, type text},
                {"State", Text.Trim, type text},
                {"DataStatus", Text.Trim, type text}
            }
        ),

    // Each connection should have only one row per day.
    UniqueKeys =
        if Table.RowCount(CleanText) <> Table.RowCount(Table.Distinct(CleanText, {"Connection", "Date"}))
        then error "Duplicate connection/date records. Check the input before loading."
        else CleanText,

    // Leave missing results empty so they are not mistaken for zero departures.
    EmptyStats =
        [departures=null, median_gap_minutes=null, longest_gap_minutes=null, first=null, last=null],
    NullRecords =
        Table.TransformColumns(
            UniqueKeys,
            {
                {"daytime", each if _ = null then EmptyStats else _, type record},
                {"evening", each if _ = null then EmptyStats else _, type record}
            }
        ),
    Daytime =
        Table.ExpandRecordColumn(
            NullRecords,
            "daytime",
            {"departures", "median_gap_minutes", "longest_gap_minutes", "first", "last"},
            {
                "DaytimeDepartures",
                "DaytimeMedianGap",
                "DaytimeLongestGap",
                "DaytimeFirst",
                "DaytimeLast"
            }
        ),
    Evening =
        Table.ExpandRecordColumn(
            Daytime,
            "evening",
            {"departures", "median_gap_minutes", "longest_gap_minutes", "first", "last"},
            {
                "EveningDepartures",
                "EveningMedianGap",
                "EveningLongestGap",
                "EveningFirst",
                "EveningLast"
            }
        ),
    TypedStats =
        Table.TransformColumnTypes(
            Evening,
            {
                {"DaytimeDepartures", Int64.Type},
                {"EveningDepartures", Int64.Type},
                {"DaytimeMedianGap", type number},
                {"EveningMedianGap", type number},
                {"DaytimeLongestGap", type number},
                {"EveningLongestGap", type number},
                {"DaytimeFirst", type datetime},
                {"DaytimeLast", type datetime},
                {"EveningFirst", type datetime},
                {"EveningLast", type datetime}
            },
            "en-US"
        ),

    // Match each date to its state, as holidays and school breaks differ.
    CalendarSource = Json.Document(File.Contents(Folder & "\data\reference\calendar_2025.json")),
    CalendarRaw = Table.FromRecords(CalendarSource[days]),
    CalendarSelected =
        Table.SelectColumns(
            CalendarRaw,
            {
                "date",
                "state",
                "public_holiday",
                "in_official_school_break",
                "additional_state_school_free_days"
            }
        ),
    CalendarRenamed =
        Table.RenameColumns(
            CalendarSelected,
            {
                {"date", "Date"},
                {"state", "State"},
                {"public_holiday", "PublicHoliday"},
                {"in_official_school_break", "RegionalSchoolBreak"},
                {"additional_state_school_free_days", "SchoolFreeDays"}
            }
        ),
    CalendarTyped =
        Table.TransformColumnTypes(
            CalendarRenamed,
            {
                {"Date", type date},
                {"State", type text},
                {"PublicHoliday", type text},
                {"RegionalSchoolBreak", type logical}
            },
            "en-US"
        ),
    CalendarUnique =
        if Table.RowCount(CalendarTyped) <> Table.RowCount(Table.Distinct(CalendarTyped, {"Date", "State"}))
        then error "Duplicate calendar date/state records."
        else CalendarTyped,
    Joined =
        Table.NestedJoin(
            TypedStats,
            {"Date", "State"},
            CalendarUnique,
            {"Date", "State"},
            "Calendar",
            JoinKind.LeftOuter
        ),
    CompleteCalendar =
        if Table.RowCount(Table.SelectRows(Joined, each Table.RowCount([Calendar]) <> 1)) > 0
        then error "A service date has no unique state calendar match."
        else Joined,
    ExpandedCalendar =
        Table.ExpandTableColumn(
            CompleteCalendar,
            "Calendar",
            {"PublicHoliday", "RegionalSchoolBreak", "SchoolFreeDays"}
        ),

    // Give public holidays priority, then separate weekends and weekdays.
    DayGroup = Table.AddColumn(ExpandedCalendar, "DayGroup", each
        if [PublicHoliday] <> null then "Public holiday"
        else if Date.DayOfWeek([Date], Day.Monday) = 5 then "Saturday"
        else if Date.DayOfWeek([Date], Day.Monday) = 6 then "Sunday"
        else if [RegionalSchoolBreak] or List.Count([SchoolFreeDays]) > 0 then "Weekday, regional school break"
        else "Weekday, outside regional school break", type text),

    // Keep the day groups in a consistent order in the charts.
    GroupOrder = Table.AddColumn(DayGroup, "DayGroupOrder", each
        if [DayGroup] = "Weekday, outside regional school break" then 1
        else if [DayGroup] = "Weekday, regional school break" then 2
        else if [DayGroup] = "Saturday" then 3
        else if [DayGroup] = "Sunday" then 4 else 5, Int64.Type),
    Month = Table.AddColumn(GroupOrder, "Month", each Date.StartOfMonth([Date]), type date),
    Result = Table.RemoveColumns(Month, {"SchoolFreeDays"})
in
    Result

