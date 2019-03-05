from flask import render_template, abort, redirect, url_for, request
from sqlalchemy.exc import DBAPIError, IntegrityError
from .forms import Company_form, Company_add_form
from .models import db, Company
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
def company_search():
    """
    POST route for /search that requests company details from API.
    """
    symbol = request.form.get('symbol')

    url = '{}/stock/{}/company'.format(os.environ.get('API_URL'), symbol)

    res = requests.get(url)
    data = json.loads(res.text)

    try:
        city = Company(name=data['companyName'])
        db.session.add(city)
        db.session.commit()
    except (DBAPIError, IntegrityError):
        abort(400)

    return redirect(url_for('.company_detail'))


@app.route('/portfolio')
def company_detail():
    """
    GET route for /portfolio that renders portfolio.html.
    """
    return render_template('portfolio.html')
