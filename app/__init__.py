import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from flask import Flask, render_template
from werkzeug.exceptions import BadRequest, InternalServerError

from . import error_handler
from .case import case
from .people import people
from .views import views


def create_app() -> 'Flask':
    """App factory"""
    app = Flask(__name__)

    load_dotenv()
    env_path = Path('..')/'.env'

    load_dotenv(dotenv_path=env_path)
    app.secret_key = os.getenv('SECRET_KEY')

    app.register_error_handler(BadRequest, error_handler.page_not_found)
    app.register_error_handler(
        InternalServerError, error_handler.internal_server_error)
    app.register_blueprint(views)
    app.register_blueprint(case, url_prefix='/case')
    app.register_blueprint(people, url_prefix='/people')

    return app
