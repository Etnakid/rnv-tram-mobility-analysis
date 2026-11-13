# rnv Tram Connections
*A personal study of tram links around Mannheim, Ludwigshafen and Heidelberg*

[English](#english) | [Deutsch](#deutsch)

## English

### Why I started this

I live in the Rhein-Neckar area. I travel by car most days, but sometimes I take the tram. I wanted to answer a local question: can I still travel between our city centres after a late shift, and how long might I wait?

I chose three central hubs so I could compare the same kind of trip in each direction. This is a small, careful study. It is not a map of every route or every way to travel between the cities.

### What I compare

The study uses 2025 timetable data from the [official rnv archive](https://gtfs-sandbox-dds.rnv-online.de/). It compares direct tram trips between:

- Mannheim Hauptbahnhof
- Ludwigshafen Berliner Platz / Bf LU Mitte
- Heidelberg Hauptbahnhof, including Hauptbahnhof West

I check all six directions between these hubs. A direct trip means the tram boards at one hub and later reaches the other on the same GTFS trip. A change is not included.

I use two time windows:

- Day: 06:00 to before 20:00
- Evening: 22:00 to 23:45, including a departure at 23:45

The evening count stops at 23:45. It does not assume that a 30-minute gap continues until 02:00.

I checked 64 historical timetable files. I leave out the 12 legal public holidays because I could not confirm which special timetable rnv used on each date. Dates with a clock change or a missing hub are marked and are not used in the medians. The number of usable dates can therefore change by direction.

A median is the middle value. I first calculate the results for each day, then compare the daily results. A median gap does not mean that every tram is exactly that many minutes apart.

### What the timetable tells us

On 2 January 2025, the archived Mannheim-to-Heidelberg timetable lists four departures in the evening window: 22:15, 22:45, 23:15 and 23:45. They are 30 minutes apart, and the last listed tram is at 23:45. This is one date, not a promise for every day. It also shows why four departures and a 30-minute gap can both be correct: the gap describes the space between trams; it does not say that service continues to 02:00.

For Mannheim to Ludwigshafen, the daytime median is 125 departures on weekdays outside school breaks and 95 on Sundays. The difference matters to people who travel at weekends. It is a reason to ask about the day type, not just the route.

Between 11 and 24 October 2025, the selected timetable has no matching direct tram trips between the Mannheim and Ludwigshafen hubs in the study windows. An [rnv construction notice](https://www.mrn-news.de/2025/10/02/ludwigshafen-sperrungen-im-bereich-berliner-platz-und-wittelsbachplatz-604990/) reports work and stop changes from 11 to 26 October. Matching trips appear again on 27 October. The notice helps explain the timetable gap, but a timetable cannot prove what ran on the street that day. [SWR also reported on the works](https://www.swr.de/swraktuell/rheinland-pfalz/ludwigshafen/haltestelle-berliner-platz-und-rhein-haardtbahn-wegen-bauarbeiten-und-gleiserneuerung-gesperrt-100.html).

In the studied windows, the archive shows no direct tram trip between the selected Ludwigshafen and Heidelberg hubs in either direction. This does not mean that a journey is impossible. A trip with a change may work; this study does not calculate it.

### Why this matters here

For someone finishing work late, the last departure can matter more than the average gap. For a weekend trip, Sunday service may be quite different from a weekday. During construction, the key question is not only “Is there a tram?” but also “Which stop is open, and where does a replacement bus leave?”

These are the next useful questions for people who live here:

- What is the last useful connection after 22:00, including a change?
- How do school breaks and Sundays change a real trip?
- Which stops and platforms are step-free, and where is that information missing?
- How do planned times compare with actual delays and cancellations?

The current analysis cannot answer all of them. It uses scheduled trips, not passenger numbers or observed arrivals. Accessibility and real-time reliability still need better data and separate checks.

### What I checked before closing this study

rnv publishes a stop plan for passengers with reduced mobility. The current plan is valid from January 2026, so it helps with travel today, but it cannot prove which platforms were step-free during 2025. It also warns that the rear part of a coupled tram may not offer step-free boarding at every stop. I have not scored the 2025 routes for accessibility.

VRN now provides public GTFS Realtime data for buses and trams. The feed can support a new study from the time collection starts. I did not find a complete historical 2025 record, so I cannot calculate yearly punctuality or cancellation rates for 2025. A timetable is not proof of what ran.

For this release, I treat the fixed-hub timetable comparison as the finished study. A full network map, a platform-by-platform accessibility check and a future real-time study are useful next projects, but they need different data.

### Reproduce the work

Use Python 3.10 or later from the project folder:

    python -m pip install -r requirements.txt
    python scripts/check_2025.py
    python scripts/annual_stops.py

The first command downloads the historical files. The scripts save raw and processed files locally; those files are not included in this repository. See [data/README.md](data/README.md), [the method](docs/methodology.md), [the calendar](docs/calendar_2025.md) and [the source notes](docs/sources.md).

The Power BI file is stored separately from this repository. The report shows the final 22:00–23:45 window, but its annual evening figures still use an earlier data import. Refresh the model before using those annual values.

This is my independent project. It is not an official rnv or VRN product. Source data keeps its own terms.

## Deutsch

### Warum ich damit angefangen habe

Ich lebe in der Rhein-Neckar-Region. An den meisten Tagen fahre ich mit dem Auto, aber manchmal nehme ich die Straßenbahn. Ich wollte eine Frage aus dem Alltag beantworten: Kann ich nach einer späten Schicht noch zwischen unseren Innenstädten fahren, und wie lange muss ich vielleicht warten?

Ich habe drei zentrale Haltestellen gewählt. So kann ich ähnliche Fahrten in beide Richtungen vergleichen. Die Studie ist bewusst klein. Sie zeigt nicht jede Linie und nicht jede mögliche Fahrt zwischen den Städten.

### Was ich vergleiche

Die Studie nutzt Fahrplandaten für 2025 aus dem [offiziellen rnv-Archiv](https://gtfs-sandbox-dds.rnv-online.de/). Verglichen werden direkte Straßenbahnfahrten zwischen:

- Mannheim Hauptbahnhof
- Ludwigshafen Berliner Platz / Bf LU Mitte
- Heidelberg Hauptbahnhof, auch Hauptbahnhof West

Ich prüfe alle sechs Richtungen zwischen diesen Haltestellen. Eine direkte Fahrt bedeutet: Die Straßenbahn fährt an einer Haltestelle los und erreicht die andere Haltestelle mit derselben GTFS-Fahrt. Umsteigen ist nicht Teil dieser Auswertung.

Ich nutze zwei Zeitfenster:

- Tag: 06:00 Uhr bis vor 20:00 Uhr
- Abend: 22:00 bis einschließlich 23:45 Uhr

Das Abendfenster endet um 23:45 Uhr. Ein Abstand von 30 Minuten bedeutet nicht, dass bis 02:00 Uhr Straßenbahnen fahren.

Ich habe 64 historische Fahrplandateien geprüft. Die 12 gesetzlichen Feiertage lasse ich aus den Berechnungen heraus, weil ich den Sonderfahrplan für diese Tage nicht sicher bestätigen konnte. Tage mit Zeitumstellung oder fehlenden Haltestellen sind markiert und gehen nicht in die Mediane ein. Deshalb kann die Zahl der nutzbaren Tage je nach Richtung anders sein.

Der Median ist der mittlere Wert. Zuerst berechne ich die Werte für jeden Tag. Dann vergleiche ich diese Tageswerte. Ein mittlerer Abstand bedeutet nicht, dass jede Straßenbahn genau so viele Minuten später kommt.

### Was der Fahrplan zeigt

Am 2. Januar 2025 stehen im archivierten Fahrplan von Mannheim nach Heidelberg vier Abendfahrten: 22:15, 22:45, 23:15 und 23:45 Uhr. Zwischen ihnen liegen 30 Minuten. Die letzte eingetragene Fahrt fährt um 23:45 Uhr. Das gilt für diesen Tag und nicht automatisch für jeden Tag. Es erklärt auch, warum vier Fahrten und ein Abstand von 30 Minuten zusammenpassen: Der Abstand beschreibt die Zeit zwischen zwei Straßenbahnen. Er sagt nicht, dass der Verkehr bis 02:00 Uhr weitergeht.

Von Mannheim nach Ludwigshafen liegt der Median am Tag bei 125 Fahrten an Werktagen außerhalb der Schulferien und bei 95 an Sonntagen. Dieser Unterschied ist für Fahrten am Wochenende wichtig. Man sollte also nicht nur nach der Linie fragen, sondern auch nach dem Wochentag.

Vom 11. bis 24. Oktober 2025 zeigt der ausgewählte Fahrplan keine passende direkte Straßenbahnfahrt zwischen den gewählten Haltestellen in Mannheim und Ludwigshafen. Eine [Baustellenmeldung von rnv](https://www.mrn-news.de/2025/10/02/ludwigshafen-sperrungen-im-bereich-berliner-platz-und-wittelsbachplatz-604990/) nennt Bauarbeiten und Änderungen an Haltestellen vom 11. bis 26. Oktober. Am 27. Oktober erscheinen wieder passende Fahrten im Fahrplan. Die Meldung hilft, die Lücke zu verstehen. Ein Fahrplan beweist aber nicht, was an diesem Tag wirklich gefahren ist. [Auch der SWR berichtete über die Bauarbeiten](https://www.swr.de/swraktuell/rheinland-pfalz/ludwigshafen/haltestelle-berliner-platz-und-rhein-haardtbahn-wegen-bauarbeiten-und-gleiserneuerung-gesperrt-100.html).

In den untersuchten Zeitfenstern zeigt das Archiv keine direkte Straßenbahnfahrt zwischen den gewählten Haltestellen in Ludwigshafen und Heidelberg, in keiner Richtung. Das heißt nicht, dass die Fahrt unmöglich ist. Mit Umsteigen kann es eine Verbindung geben; diese Studie berechnet sie nicht.

### Was das für Menschen hier bedeutet

Wer spät Feierabend hat, braucht oft die letzte passende Verbindung. Der mittlere Abstand allein reicht dafür nicht. Am Wochenende kann der Fahrplan anders sein als an einem Werktag. Bei einer Baustelle ist auch wichtig: Welche Haltestelle ist offen, und wo fährt ein Ersatzbus ab?

Das sind gute nächste Fragen für Menschen aus der Region:

- Welche Verbindung gibt es nach 22:00 Uhr noch, auch mit Umsteigen?
- Was ändert sich an Sonntagen und in den Schulferien?
- Welche Haltestellen und Bahnsteige sind stufenfrei, und wo fehlen Informationen?
- Wie unterscheiden sich Fahrplan und tatsächliche Verspätungen oder Ausfälle?

Die aktuelle Auswertung kann noch nicht alles beantworten. Sie nutzt geplante Fahrten, aber keine Fahrgastzahlen und keine gemessenen Ankunftszeiten. Für Barrierefreiheit und Zuverlässigkeit brauche ich bessere Daten und eigene Prüfungen.

### Was ich vor dem Abschluss noch geprüft habe

rnv veröffentlicht einen Haltestellenplan für Fahrgäste mit eingeschränkter Mobilität. Der aktuelle Plan gilt ab Januar 2026. Er hilft bei der heutigen Fahrt, zeigt aber nicht sicher, welche Bahnsteige 2025 stufenfrei waren. Der Plan weist auch darauf hin: Bei gekoppelten Straßenbahnen ist ein stufenfreier Einstieg im hinteren Teil nicht an jeder Haltestelle möglich. Für 2025 habe ich die Bahnsteige nicht bewertet.

VRN bietet jetzt öffentliche GTFS-Echtzeitdaten für Busse und Straßenbahnen an. Damit kann man ab Beginn einer eigenen Datensammlung eine neue Studie machen. Ich habe kein vollständiges Archiv für 2025 gefunden. Deshalb kann ich für 2025 keine Jahreswerte zu Verspätungen oder Ausfällen berechnen. Ein Fahrplan beweist nicht, was wirklich gefahren ist.

Für diese Version ist der Fahrplanvergleich an den festen Haltestellen abgeschlossen. Eine vollständige Netzkarte, eine Prüfung jedes Bahnsteigs und eine spätere Echtzeitstudie sind sinnvolle neue Projekte. Dafür brauche ich andere Daten.

### So kann man die Auswertung wiederholen

Python 3.10 oder neuer im Projektordner:

    python -m pip install -r requirements.txt
    python scripts/check_2025.py
    python scripts/annual_stops.py

Der erste Befehl lädt die historischen Dateien herunter. Die Skripte speichern Rohdaten und Ergebnisse nur lokal; sie sind nicht in diesem Repository. Mehr steht in [data/README.md](data/README.md), [der Methode](docs/methodology.md), [dem Kalender](docs/calendar_2025.md) und [den Quellen](docs/sources.md).

Die Power-BI-Datei liegt getrennt von diesem Repository. Im Bericht steht das endgültige Zeitfenster 22:00–23:45, aber die Abendwerte für das ganze Jahr stammen noch aus einem älteren Datenimport. Vor der Nutzung dieser Jahreswerte muss das Modell neu geladen werden.

Das ist mein eigenes Projekt, kein offizielles Produkt von rnv oder VRN. Für die Quelldaten gelten die jeweiligen Nutzungsbedingungen.
