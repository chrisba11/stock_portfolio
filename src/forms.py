from flask import g
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField
from wtforms.validators import DataRequired
from .models import Portfolio


class CompanyForm(FlaskForm):
    """
    Class to create a form with a field for a company symbol.
    """
    symbol = StringField('symbol', validators=[DataRequired()])


class CompanyAddForm(FlaskForm):
    """
    Class to create a form for adding a company to the database.
    """
    symbol = StringField('symbol', validators=[DataRequired()])
    company_name = StringField('company name', validators=[DataRequired()])
    portfolios = SelectField('portfolios')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.portfolios.choices = [(str(p.id), p.portfolio_name) for p in Portfolio.query.filter_by(user_id=g.user.id).all()]


class PortfolioAddForm(FlaskForm):
    """
    Class to create a new portfolio name.
    """
    portfolio_name = StringField('Portfolio Name', validators=[DataRequired()])


class AuthForm(FlaskForm):
    """
    Class to create a form for user registration and login.
    """
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
