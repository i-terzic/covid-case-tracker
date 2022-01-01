from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route('/')
@views.route('/home')
def home() -> 'render_template':
    return render_template('home.html',  title='Home')
