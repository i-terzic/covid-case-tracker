import os

import pymssql
import requests
from flask import Blueprint, jsonify, redirect, render_template, request

from .database import DatabaseConnection

views = Blueprint("views", __name__)


@views.route('/')
@views.route('/home')
def home() -> 'render_template':
    return render_template('index.html', name='Ivan', title='Home')


@views.route('/500')
def test_500() -> 'render_template':
    meme_path = os.path.join('static', '500.png')
    return render_template('500.html', name='500', meme_path=meme_path)
