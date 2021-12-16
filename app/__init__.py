import json
import os

import requests
from flask import Flask, render_template

from .case import case
from .views import views


def create_app() -> 'Flask':
    """App factory"""
    app = Flask(__name__)

    app.register_blueprint(views)
    app.register_blueprint(case, url_prefix='/case')

    @app.errorhandler(404)
    def page_not_found(e) -> 'render_template':
        res = requests.get('https://api.chucknorris.io/jokes/random').text
        joke = json.loads(res).get('value')
        return render_template('404.html', name='404', joke=joke), 404

    @app.errorhandler(500)
    def internal_server_error(e) -> 'render_template':
        meme_path = os.path.join('static', '500.png')
        return render_template('500.html', name='500',  meme_path=meme_path), 500

    return app
