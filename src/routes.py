from flask import render_template, abort, redirect, url_for, request
from sqlalchemy.exc import DBAPIError, IntegrityError
from .models import db, City
from . import app
import json
import os
import requests


@app.route('/')
def home():
    """

    """
    return render_template('home.html')


