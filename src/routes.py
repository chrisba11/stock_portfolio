from flask import render_template, redirect, url_for, request, session, flash, g
from sqlalchemy.exc import DBAPIError, IntegrityError, InvalidRequestError
from json.decoder import JSONDecodeError
from .auth import login_required
from .forms import CompanyForm, CompanyAddForm, PortfolioAddForm
from .models import db, Company, Portfolio
from . import app
import json
import os
import requests


@app.add_template_global
def get_portfolios():
    """

    """
    if g.user is not None:
        return Portfolio.query.filter_by(user_id=g.user.id).all()

    return 'get_portfolios DIDNT WORK!'


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
    form = CompanyForm()

    if form.validate_on_submit():
        try:
            symbol = form.data['symbol']

            url = '{}/stock/{}/company'.format(os.getenv('API_URL'), symbol)

            res = requests.get(url)
            data = json.loads(res.text)

            session['context'] = data
            session['symbol'] = symbol

        except JSONDecodeError:
            flash("That symbol doesn't seem to exist")

            return render_template('search.html', form=form)

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

    form = CompanyAddForm(**form_context)

    if form.validate_on_submit():

        if Company.query.filter_by(symbol=form_context['symbol']).first() is None:
            try:
                company = Company(
                    company_name=form_context['company_name'],
                    symbol=form_context['symbol'],
                    portfolio_id=form.data['portfolios']
                )
                db.session.add(company)
                db.session.commit()
            except (DBAPIError, InvalidRequestError):
                flash('Oops. That company appears to already exist in the database. Please choose another.')

                return render_template('search.html', form=form)

            except IntegrityError:
                flash('Something went wrong. SAD!')

                return render_template('search.html', form=form)

            return redirect(url_for('.company_detail'))
        else:
            flash('Oops. That company appears to already exist in the database. Please choose another.')

            return render_template('search.html', form=form)

    return render_template(
        'company.html',
        form=form,
        company_name=form_context['company_name'],
        symbol=form_context['symbol']
    )


@app.route('/portfolio', methods=['GET', 'POST'])
def company_detail():
    """
    GET route for /portfolio that renders portfolio.html.
    """
    form = PortfolioAddForm()

    if form.validate_on_submit():
        try:
            porfolio = Portfolio(portfolio_name=form.data['portfolio_name'], user_id=g.user.id)
            db.session.add(porfolio)
            db.session.commit()
        except (DBAPIError, IntegrityError):
            flash('Oops. That portfolio name appears to already exist in the database. Please choose another.')

            return render_template('portfolio.html', form=form)

        return redirect(url_for('.company_search'))

    user_portfolios = Portfolio.query.filter(Portfolio.user_id == g.user.id).all()
    portfolio_ids = [port.id for port in user_portfolios]
    user_companies = Company.query.filter(Company.portfolio_id.in_(portfolio_ids)).all()

    return render_template('portfolio.html', companies=user_companies, form=form, portfolios=user_portfolios)
