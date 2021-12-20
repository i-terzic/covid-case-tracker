import os

import pymssql
import requests
from flask import Blueprint, jsonify, redirect, render_template, request

from .database import DatabaseConnection

views = Blueprint("views", __name__)


@views.route('/')
@views.route('/home')
def home() -> 'render_template':
    return render_template('home.html',  title='Home')
