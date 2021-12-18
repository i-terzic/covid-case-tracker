# Covid-Case Tracker App with remote DB connection

## Installation

### Requirements

- [ ] Python 3.x

- [ ] Git

- [ ] Internet connection (for API access and CDN access)

- [ ] VPN Connection to HS VPN

On Linux/Mac run:

```
python3 -m venv venv

source venv/bin/activate

python3 -m pip install -r requirements.txt
```

On Windows run:

```
python3 -m venv venv

venv\Scripts\activate.bat

python3 -m pip install -r requirements.txt
```

to create a virtual environment and install all requirements.

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
  - Art (char(64) ggf. m. Domäne)
  - Ergebnis (char(64) ggf. m Donäne)
  - Datum (date)
- Covid-Fall:
  - PK: id (int)
  - FK: person.id (int)
  - Testergebnis (char(64) ggf. m. Domäne)
  - Testdatum (date)
  - Quarantänedatum (date)
