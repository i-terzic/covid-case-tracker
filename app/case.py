from flask import Blueprint, redirect, render_template, request
from flask.helpers import url_for
from flask.typing import StatusCode

from .database import DatabaseConnection

case = Blueprint('case', __name__)


@case.route('/new')
def new_case() -> 'render_template':
    """render the new case template"""
    if request.method == 'POST':  # TODO end post request with redirect
        pass
    if request.method == 'GET':
        return render_template('new_case.html', title='New Case')


@case.route('/open')
def open_case() -> 'render_template':
    if request.method == 'POST':  # TODO end post request with redirect
        pass
    if request.method == 'GET':
        try:
            with DatabaseConnection() as cur:
                cur.execute(
                    "SELECT * FROM terzic_case WHERE status = 'open';")
                data = []
                for line in cur:
                    case = dict(line)
                    data.append(case)
        except Exception as err:
            return render_template('500.html'), 500
        return render_template('open_case.html', title='Open Cases', cases=data)


@case.route('/closed')
def closed_case() -> 'render_template':
    if request.method == 'POST':  # TODO end post request with redirect
        pass
    if request.method == 'GET':
        try:
            with DatabaseConnection() as cur:
                cur.execute(
                    "SELECT * FROM terzic_case WHERE status = 'closed';"
                )
                data = []
                for line in cur:
                    case = dict(line)
                    data.append(case)
        except Exception as err:
            return render_template('500.html', 500)
        return render_template('closed_case.html', title='Closed Cases', cases=data)
