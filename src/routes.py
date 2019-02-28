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
    GET route for / that renders home.html.
    """
    return render_template('home.html')


@app.route('/search')
def company_search_form():
    """
    GET route for /search that renders search.html.
    """
    return render_template('search.html')


@app.route('/search', methods=['POST'])
def company_search_results():
    """
    POST route for /search that requests company details from API.
    """
    zipcode = request.form.get('zipcode')

    url = '{}/company?zip={}&APPID={}'.format(
        os.environ.get('API_URL'),
        zipcode,
        os.environ.get('API_KEY')
    )

    res = request.get(url)
    data = json.loads(res.text)

    try:
        city = City(name=data['name'], zipcode=zipcode)
        db.session.add(city)
        db.session.commit()
    except (DBAPIError, IntegrityError):
        abort(400)

    return redirect(url_for('.company_detail'))


@app.route('/company')
def company_detail():
    """
    GET route for /company that renders company.html.
    """
    return render_template('company.html')
