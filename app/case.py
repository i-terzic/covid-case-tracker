from flask import Blueprint, render_template, request

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
        cases = [str(x) + ' open case' for x in range(10)]
        return render_template('open_case.html', title='Open Cases', cases=cases)


@case.route('/closed')
def closed_case() -> 'render_template':
    if request.method == 'POST':  # TODO end post request with redirect
        pass
    if request.method == 'GET':
        cases = [str(x) + ' closed case' for x in range(10)]
        return render_template('closed_case.html', title='Closed Cases', cases=cases)
