import json
import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_cors import CORS
from werkzeug.exceptions import InternalServerError, NotFound

from . import error_handler
from .api import api
from .case import case
from .people import people
from .views import views


def create_app() -> 'Flask':
    """App factory"""
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    load_dotenv()
    env_path = Path('..')/'.env'

    load_dotenv(dotenv_path=env_path)
    app.secret_key = os.getenv('SECRET_KEY')

    app.register_error_handler(NotFound, error_handler.page_not_found)
    app.register_error_handler(
        InternalServerError, error_handler.internal_server_error)
    app.register_blueprint(views)
    app.register_blueprint(case, url_prefix='/case')
    app.register_blueprint(people, url_prefix='/people')
    app.register_blueprint(api, url_prefix='/api')

    return app
