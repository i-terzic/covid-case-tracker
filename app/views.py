import os

import pymssql
import requests
from flask import Blueprint, jsonify, redirect, render_template

from .database import DB_CONFIG, DatabaseConnection

views = Blueprint(name="views", import_name=__name__)


@views.route('/')
@views.route('/home')
def home() -> 'render_template':
    """render the home template"""
    return render_template('index.html', name='Ivan', title='Home')


@views.route('/newcase')
def new_case() -> 'render_template':
    """render the new case template"""
    return render_template('new_case.html')
