"""API endpoint file"""
from flask import Blueprint, jsonify
from flask_cors import cross_origin
from werkzeug.exceptions import InternalServerError

from .database import DatabaseConnection

api = Blueprint('api', __name__)


@api.route('/cases')
@cross_origin()  # allow cors policy
def cases() -> 'jsonify':
    """Cross-origin endpoint to retrieve the count of cases by date"""
    try:
        with DatabaseConnection() as cur:
            data = []
            _sql = """  SELECT count(*) as count, date as date
                        FROM terzic_case
                        GROUP BY date;"""
            cur.execute(_sql)
            for line in cur:
                data.append(dict(line))
    except Exception as err:
        raise InternalServerError() from err
    return jsonify(data)
