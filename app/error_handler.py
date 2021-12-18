import requests
from flask import Blueprint, json, render_template

error = Blueprint('error', __name__)


@error.errorhandler(404)
def page_not_found(e) -> 'render_template':
    res = requests.get('https://api.chucknorris.io/jokes/random').text
    joke = json.loads(res).get('value')
    return render_template('404.html', name='404', joke=joke), 404


@error.errorhandler(500)
def internal_server_error(e) -> 'render_template':
    return render_template('500.html', name='500'), 500
