"""Build the 2025 state-level calendar from reviewed official dates."""
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data' / 'reference'
OUT.mkdir(parents=True, exist_ok=True)
SOURCES = {
    'kmk_2024_25': 'https://www.kmk.org/fileadmin/Dateien/pdf/Ferienkalender/FER2024_25.pdf',
    'kmk_2025_26': 'https://www.kmk.org/fileadmin/Dateien/pdf/Ferienkalender/FER2025_26.pdf',
    'BW_holidays': 'https://im.baden-wuerttemberg.de/de/service/feiertage',
    'RP_holidays': 'https://mdi.rlp.de/themen/buerger-und-staat/verfassung-und-verwaltung/sonn-und-feiertagsrecht',
    'HE_holidays': 'https://innen.hessen.de/buerger-staat/feiertage',
    'BW_school': 'https://km.baden-wuerttemberg.de/de/service/ferien',
    'RP_school': 'https://bm.rlp.de/service/ferientermine/seite',
    'HE_local': 'https://schulaemter.hessen.de/Themen-A-Z/ferien',
}
COMMON = [
    ('2025-01-01', 'Neujahr'), ('2025-04-18', 'Karfreitag'),
    ('2025-04-21', 'Ostermontag'), ('2025-05-01', 'Tag der Arbeit'),
    ('2025-05-29', 'Christi Himmelfahrt'), ('2025-06-09', 'Pfingstmontag'),
    ('2025-06-19', 'Fronleichnam'), ('2025-10-03', 'Tag der Deutschen Einheit'),
    ('2025-12-25', '1. Weihnachtsfeiertag'), ('2025-12-26', '2. Weihnachtsfeiertag'),
]
HOLIDAYS = {state: dict(COMMON) for state in ('BW', 'RP', 'HE')}
HOLIDAYS['BW']['2025-01-06'] = 'Erscheinungsfest'
for state in ('BW', 'RP'):
    HOLIDAYS[state]['2025-11-01'] = 'Allerheiligen'
BREAKS = {
    'BW': [('Christmas 2024/25','2024-12-23','2025-01-04'), ('Easter','2025-04-14','2025-04-26'), ('Pentecost','2025-06-10','2025-06-20'), ('Summer','2025-07-31','2025-09-13'), ('Autumn','2025-10-27','2025-10-30'), ('Christmas 2025/26','2025-12-22','2026-01-05')],
    'RP': [('Christmas 2024/25','2024-12-23','2025-01-08'), ('Easter','2025-04-14','2025-04-25'), ('Summer','2025-07-07','2025-08-15'), ('Autumn','2025-10-13','2025-10-24'), ('Christmas 2025/26','2025-12-22','2026-01-07')],
    'HE': [('Christmas 2024/25','2024-12-23','2025-01-10'), ('Easter','2025-04-07','2025-04-21'), ('Summer','2025-07-07','2025-08-15'), ('Autumn','2025-10-06','2025-10-18'), ('Christmas 2025/26','2025-12-22','2026-01-10')],
}
events = []
daily = []
for state in HOLIDAYS:
    for day, name in sorted(HOLIDAYS[state].items()):
        events.append(dict(state=state, kind='public_holiday', name=name, start=day, end=day, source=state+'_holidays'))
    for name, start, end in BREAKS[state]:
        events.append(dict(state=state, kind='school_break', name=name, start=start, end=end, source='kmk_2025_26' if start >= '2025-10-01' else 'kmk_2024_25'))
    if state == 'BW':
        events.append(dict(state=state, kind='school_free_day', name='Reformationsfest', start='2025-10-31', end='2025-10-31', source='BW_school'))
    for offset in range(365):
        day = dt.date(2025,1,1) + dt.timedelta(days=offset)
        iso = day.isoformat()
        breaks = [name for name, start, end in BREAKS[state] if start <= iso <= end]
        school_free = ['Reformationsfest'] if state == 'BW' and iso == '2025-10-31' else []
        daily.append(dict(date=iso, state=state, weekday=day.isoweekday(), is_weekend=day.weekday() >= 5, public_holiday=HOLIDAYS[state].get(iso), in_official_school_break=bool(breaks), school_break_names=breaks, additional_state_school_free_days=school_free, local_school_closure=None))
assert len(daily) == 1095
assert len({(r['state'], r['date']) for r in daily}) == 1095
assert {s: len(h) for s,h in HOLIDAYS.items()} == {'BW':12,'RP':11,'HE':10}
assert next(r for r in daily if r['state']=='BW' and r['date']=='2025-10-31')['public_holiday'] is None
meta = dict(year=2025, reviewed_on='2026-10-22', sources=SOURCES, limitations=['Statewide dates only; local movable school days and exceptional closures remain unknown.', 'Break intervals are inclusive; weekends and public holidays retain independent flags.', 'No inferred is_school_day flag: absence from an official break does not prove classes were held.', 'Use as explanatory context, not to override GTFS service calendars.'])
for name, content in [('calendar_2025.json',dict(metadata=meta,days=daily)),('calendar_events_2025.json',dict(metadata=meta,events=events))]:
    (OUT/name).write_text(json.dumps(content,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines = ['# Calendario di riferimento 2025', '', 'Ambito: rete tranviaria rnv nei Länder Baden-Württemberg (BW), Rheinland-Pfalz (RP), Hessen (HE). Date iniziali e finali incluse. Verificato il 22 ottobre 2026.', '', '## Festività legali', '', '| Data | Ricorrenza | Länder |', '|---|---|---|']
for day in sorted({d for h in HOLIDAYS.values() for d in h}):
    states = [s for s,h in HOLIDAYS.items() if day in h]
    lines.append('| '+day+' | '+HOLIDAYS[states[0]][day]+' | '+', '.join(states)+' |')
lines += ['', '## Vacanze scolastiche ufficiali', '', '| Periodo | Baden-Württemberg | Rheinland-Pfalz | Hessen |', '|---|---|---|---|']
for label in ['Christmas 2024/25','Easter','Pentecost','Summer','Autumn','Christmas 2025/26']:
    row = [label]
    for state in ('BW','RP','HE'):
        match = [(start,end) for name,start,end in BREAKS[state] if name==label]
        row.append(' / '.join(match[0]) if match else 'Nessuna pausa regionale prevista')
    lines.append('| '+' | '.join(row)+' |')
lines += ['', 'Il 31 ottobre 2025 in BW è senza lezioni (Reformationsfest), ma non è una festività legale generale. È registrato separatamente dalle vacanze autunnali del 27–30 ottobre.', '', '## Limiti e uso', '', '- Il file giornaliero contiene 365 date per ciascuno dei tre Länder (1.095 righe logiche).', '- Le vacanze natalizie che attraversano il confine annuale mantengono gli intervalli originali; il calendario giornaliero è limitato al 2025.', '- Sabati, domeniche, festivi e vacanze hanno indicatori separati e possono sovrapporsi.', '- I giorni mobili locali (per esempio Carnevale o ponti) e le chiusure eccezionali sono ancora da verificare presso scuole e autorità competenti. Non sono automaticamente giorni di lezione.', '- Il 24 e il 31 dicembre non sono festività legali generali: eventuali orari speciali vanno letti nei dati rnv.', '- Calendari universitari e scuole con regimi speciali non sono compresi.', '- Per le linee che attraversano più Länder si conservano tutti e tre i calendari; non si assegna un solo calendario a tutta la linea.', '- Queste variabili aiutano a interpretare il servizio: il calendario GTFS resta la fonte delle corse attive.', '', '## Fonti ufficiali', '']
lines += ['- ['+key+']('+url+')' for key,url in SOURCES.items()]
(ROOT/'docs'/'calendar_2025.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Generated 1,095 state-date records and',len(events),'events; integrity checks passed.')
