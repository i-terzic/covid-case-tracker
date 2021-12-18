from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug.exceptions import InternalServerError

from .database import DatabaseConnection

people = Blueprint('people', __name__)


@people.route('/all')
def all() -> 'render_template':
    if request.method == 'POST':
        return redirect('500.html'), 500
    if request.method == 'GET':
        try:
            with DatabaseConnection() as cur:
                cur.execute('SELECT * FROM terzic_people')
        except Exception as err:
            raise InternalServerError()
    return render_template('people.html', title='Person')
