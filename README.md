# Covid-Case Tracker App mit remote DB connection

## Installation

### Requirements

- [ ] Python 3.x

- [ ] Git

- [ ] Internet Zugang (für API und CDN Zugang)

- [ ] VPN Connection zum HS VPN (andernfalls funktioniert die App nicht richtig, da keine Daten zur verfügung stehen)

Linux/Mac:

```
python3 -m venv venv

source venv/bin/activate

python3 -m pip install -r requirements.txt
```

Im Anschluss muss ggf. unter `venv/lib/flask_script/__init__.py` die Zeile

```
from flask._compat import text_type
```

mit

```
from flask_script._compat import text_type
```

ausgetauscht werden.\
Windows (command prompt):

```
python3 -m venv venv

venv\Scripts\activate.bat

pip install -r requirements.txt
```

Im Anschluss muss ggf. unter `venv\lib\site-packages\flask_script\__init__.py` die Zeile

```
from flask._compat import text_type
```

mit

```
from flask_script._compat import text_type
```

ausgetauscht werden.\

um eine virtual environment zu erstellen und alle requrements zu installieren.

Im Anschluss muss eine `.env`-Datei erstellt werden.
Die relevanten Felder sind in der `.sample.env`-Datei aufgeführt.

Die Applikation kann mittels

```
python3 manage.py runserver -d
```

ausgeführt werden und läuft unter.

```
http://localhost:5000
```

## Data Model

- Person:
  - PK: id (int)
  - Vorname (char(64))
  - Name (char(64))
  - Geburtsdatum (date)
  - Adresse (char(64))
- Test:
  - PK: id (int)
  - FK: Person.id (int)
  - Art (char(64))
  - Ergebnis (char(64))
  - Datum (date)
- Covid-Fall:
  - PK: id (int)
  - FK: person.id (int)
  - FK: test.id (int)
  - Quarantäne-Start (date)
  - Quarantäne-Ende (date)
  - Status (char(64))

## Funktionsweise

- Views:
  - Home:
    - Zeigt einen Graphen mit der Anzahl an Fällen in den letzten 7 Tagen an
  - People:
    - Zeigt alle getesteten Personen an mit allen relevanten Informationen
  - New Case:
    - Hier können neue Covid-19 Fälle bzw. Test erstellt werden.
    - Die Logik berücksichtigt auch ob das resultat Positiv oder Negativ war und fordert dementsprechend ein Start- und Enddatum für die Qarantäne
    - Ein Fall entspricht einem Test
    - Fällt der Test negativ aus ist der Fall direkt geschlossen und unter Cases > Closed Cases zu finden
    - Fällt der Test positiv aus ist der Fall offen und kann unter Cases > Open Cases geschlossen werden, oder die Quarantäne kann um 1 Woche verlängert werden
  - Open cases
    - Zeigt alle offenen Cases an
    - die Quarantäne kann um 1 Woche verlängert werden, oder der Fall wird geschlossen
  - Closed cases:
    - Zeigt alle geschlossenen Cases an, auch die Historie falls eine Person mehrere Cases hatte
