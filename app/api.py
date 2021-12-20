from flask import Blueprint, jsonify
from werkzeug.exceptions import InternalServerError

from .database import DatabaseConnection

api = Blueprint('api', __name__)


@api.route('/cases')
def cases() -> 'jsonify':
    try:
        with DatabaseConnection() as cur:
            data = []
            _SQL = """  SELECT count(*) as count, date as date
                        FROM terzic_case
                        GROUP BY date;"""
            cur.execute(_SQL)
            for line in cur:
                data.append(dict(line))
    except Exception as err:
        print(err)
        raise InternalServerError()
    return jsonify(data)
