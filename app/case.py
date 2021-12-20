
from flask import Blueprint, flash, redirect, render_template, request
from werkzeug.exceptions import InternalServerError

from .database import DatabaseConnection
from .utils import FormHandler

case = Blueprint('case', __name__)


@case.route('/new', methods=['GET', 'POST'])
def new_case() -> 'render_template':
    """render the new case template"""
    if request.method == 'POST':
        try:
            with DatabaseConnection() as cur:
                _SQL = FormHandler.create_new_case_query(dict(request.form))
                cur.execute(_SQL)
                flash('Successfully submited new Case', category='success')
        except Exception as err:
            print(err)
            flash('Please try again', category='danger')
            raise InternalServerError()
        return render_template('new_case.html', title='New Case')
    if request.method == 'GET':
        return render_template('new_case.html', title='New Case')


@case.route('/open', methods=['GET', 'POST'])
def open_case() -> 'render_template':
    if request.method == 'POST':  # TODO
        if id := request.form.get('close'):
            print(request.form.get('close'))
            flash(f'Case: {id} successfully closed!', category='success')
        elif id := request.form.get('extend'):
            print(request.form.get('close'))
            flash(f'Quarantine of case: {id} extended!', category='warning')
        return redirect('open')
    if request.method == 'GET':
        try:
            with DatabaseConnection() as cur:
                cur.execute(
                    """EXEC terzic_get_cases 'open';"""
                )
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
                    """EXEC terzic_get_cases 'closed';"""
                )
                data = []
                for line in cur:
                    case = dict(line)
                    data.append(case)
        except Exception as err:
            raise InternalServerError()
        return render_template('closed_case.html', title='Closed Cases', cases=data)
