import pprint

from app import database as db
from app.form_handler import FormHandler

if __name__ == '__main__':
    with db.DatabaseConnection() as cur:
        try:
            data = dict([('last-name', 'Terzic'), ('first-name', 'Ivan'), ('birth-date', '2021-02-02'), ('address', 'Lmao'),
                        ('test-date', '2021-01-01'), ('test-result', 'negativ'), ('quarantine-start-date', ''), ('quarantine-end-date', '')])

            _SQL = FormHandler.create_new_case_query(data)
            cur.execute(_SQL)
        except Exception as err:
            raise Exception(err)
