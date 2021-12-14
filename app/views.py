import os

from flask import Blueprint, redirect, render_template

views = Blueprint(name="views",import_name=__name__)


@views.route('/')
@views.route('/home')
def home() ->'render_template':
    return render_template('index.html', name='Ivan', title='Home')


@views.route('/newcase')
def new_case() -> 'render_template':
    return render_template('new_case.html')

@views.route('/500')
def test_500() ->'render_template':
    meme_path = os.path.join('static', '500.png')
    return render_template('500.html',meme_path=meme_path)

