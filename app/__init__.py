import json
import os

import requests
from flask import Flask, render_template
from werkzeug.exceptions import BadRequest, InternalServerError

from . import error_handler
from .case import case
from .people import people
from .views import views


def create_app() -> 'Flask':
    """App factory"""
    app = Flask(__name__)

    app.register_error_handler(BadRequest, error_handler.page_not_found)
    app.register_error_handler(
        InternalServerError, error_handler.internal_server_error)
    app.register_blueprint(views)
    app.register_blueprint(case, url_prefix='/case')
    app.register_blueprint(people, url_prefix='/people')

    return app
