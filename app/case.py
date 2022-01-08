"""Case related endpoints"""
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
                _sql = FormHandler.create_new_case_query(dict(request.form))
                cur.execute(_sql)
                flash('Successfully submited new Case', category='success')
        except Exception as err:
            flash('Please try again', category='danger')
            raise InternalServerError() from err
        return render_template('new_case.html', title='New Case')
    return render_template('new_case.html', title='New Case')


@case.route('/open', methods=['GET', 'POST'])
def open_case() -> 'render_template':
    """render the open case template"""
    if request.method == 'POST':
        if case_id := request.form.get('close'):
            try:
                with DatabaseConnection() as cur:
                    cur.execute(f"""EXEC terzic_close_case {case_id};""")
                    flash(f'Case: {case_id} successfully closed',
                          category='success')
            except Exception as err:
                flash('Cannot close case - please try again!', category='danger')
                raise InternalServerError() from err
        elif case_id := request.form.get('extend'):
            try:
                with DatabaseConnection() as cur:
                    cur.execute(
                        f"""EXEC terzic_extend_quarantine {case_id}; """)
                    flash(
                        f'Quarantine of case: {case_id} extended!', category='warning')
            except Exception as err:
                flash('Cannot extend quarantine!', category='danger')
                raise InternalServerError() from err
        return redirect('open')
    try:
        with DatabaseConnection() as cur:
            cur.execute(
                """EXEC terzic_get_cases 'open';"""
            )
            data = []
            for line in cur:
                data.append(dict(line))
    except Exception as err:
        raise InternalServerError() from err
    return render_template('open_case.html', title='Open Cases', cases=data)


@case.route('/closed')
def closed_case() -> 'render_template':
    """render closed_cases.html template"""
    try:
        with DatabaseConnection() as cur:
            cur.execute(
                """EXEC terzic_get_cases 'closed';"""
            )
            data = []
            for line in cur:
                data.append(dict(line))
    except Exception as err:
        raise InternalServerError() from err
    return render_template('closed_case.html', title='Closed Cases', cases=data)
