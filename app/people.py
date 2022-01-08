"""People related endpoints"""
from flask import Blueprint, redirect, render_template, request
from werkzeug.exceptions import InternalServerError

from .database import DatabaseConnection

people = Blueprint('people', __name__)


@people.route(rule='/all', methods=['GET'])
def people_all() -> 'render_template':
    """Render people.html template"""
    if request.method == 'POST':
        return redirect('500.html'), 500
    if request.method == 'GET':
        try:
            with DatabaseConnection() as cur:
                cur.execute('SELECT * FROM terzic_person')
                data = []
                for line in cur:
                    data.append(dict(line))
        except Exception as err:
            raise InternalServerError() from err
    return render_template('people.html', title='Person', people=data)
