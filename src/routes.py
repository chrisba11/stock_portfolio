from flask import render_template, redirect, url_for, request, session, flash
from sqlalchemy.exc import DBAPIError, IntegrityError
from .forms import Company_form, Company_add_form, Portfolio_add_form
from .models import db, Company, Portfolio
from . import app
import json
import os
import requests


@app.add_template_global
def get_portfolios():
    """

    """
    return Portfolio.query.all()


@app.route('/')
def home():
    """
    GET route for / that renders home.html.
    """
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
def company_search():
    """
    GET & POST routes for /search that requests company details from API.
    """
    form = Company_form()

    if form.validate_on_submit():
        symbol = form.data['symbol']

        url = '{}/stock/{}/company'.format(os.getenv('API_URL'), symbol)

        res = requests.get(url)
        data = json.loads(res.text)

        session['context'] = data
        session['symbol'] = symbol

        return redirect(url_for('.company_preview'))

    return render_template('search.html', form=form)


@app.route('/preview', methods=['GET', 'POST'])
def company_preview():
    """

    """
    form_context = {
        'company_name': session['context']['companyName'],
        'symbol': session['symbol']
    }

    form = Company_add_form(**form_context)

    if form.validate_on_submit():
        try:
            company = Company(
                company_name=form_context['company_name'],
                symbol=form_context['symbol']
            )
            db.session.add(company)
            db.session.commit()
        except (DBAPIError, IntegrityError):
            flash('Oops. Something went wrong with your search.')
            return render_template('search.html', form=form)

        return redirect(url_for('.company_detail'))

    return render_template(
        'company.html',
        form=form,
        company_name=form_context['company_name'],
        symbol=form_context['symbol']
    )


@app.route('/portfolio')
def company_detail():
    """
    GET route for /portfolio that renders portfolio.html.
    """
    form = Portfolio_add_form()

    if form.validate_on_submit():
        try:
            porfolio = Portfolio(portfolio_name=form.data['portfolio_name'])
            db.session.add(porfolio)
            db.session.commit()
        except (DBAPIError, IntegrityError):
            flash('Oops. Something went wrong with your portfolio form.')
            return render_template('portfolio.html', form=form)
        return redirect(url_for('.company_search'))

    companies = Company.query.all()
    return render_template('portfolio.html', companies=companies, form=form)
