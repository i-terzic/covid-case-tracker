import re

from flask import Blueprint, flash, redirect, render_template, request
from flask.helpers import url_for
from flask.typing import StatusCode
from werkzeug.exceptions import InternalServerError

from .database import DatabaseConnection

case = Blueprint('case', __name__)


# @first_name char(64),
# @last_name char(64),
# @birth_date date,
# @address char(64),

# @test_type char(64),
# @test_result char(64),
# @test_date date,

# @q_start_date date,
# @q_end_date date,
# @q_status char(64)

@case.route('/new', methods=['GET', 'POST'])
def new_case() -> 'render_template':
    """render the new case template"""
    if request.method == 'POST':  # TODO
        try:
            with DatabaseConnection() as cur:
                first_name = request.form.get('first-name')
                last_name = request.form.get('last-name')
                birth_date = request.form.get('birth-date')
                address = request.form.get('address')

                test_type = request.form.get('test-type')
                test_result = request.form.get('test-result')
                test_date = request.form.get('test-date')

                q_start_date = request.form.get('quarantine-start-date') if test_result != 'negativ' else 'NULL'
                q_end_date = request.form.get('quarantine-end-date') if test_result != 'negativ' else 'NULL'
                q_status = 'closed' if q_start_date is None else 'open'
                _SQL = f""" EXEC terzic_create_case 
                            @first_name={first_name}, 
                            @last_name={last_name},
                            @
                                                    """
                cur.execute()
            flash('Successfully submited new Case', category='success')
        except Exception as err:
            flash('Please try again', category='danger')
            raise InternalServerError()
        return render_template('new_case.html', title='New Case')
    if request.method == 'GET':
        return render_template('new_case.html', title='New Case')


@case.route('/open')
def open_case() -> 'render_template':
    if request.method == 'POST':  # TODO
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
            raise InternalServerError()
        return render_template('open_case.html', title='Open Cases', cases=data)


@case.route('/closed')
def closed_case() -> 'render_template':
    if request.method == 'POST':  # TODO
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
            raise InternalServerError()
        return render_template('closed_case.html', title='Closed Cases', cases=data)
