from flask import Blueprint, render_template, request

people = Blueprint('people', __name__)


@people.route('/all')
def people_all() -> 'render_template':
    pass
