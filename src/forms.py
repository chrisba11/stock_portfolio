from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class Company_form(FlaskForm):
    """

    """
    symbol = StringField('symbol', validators=[DataRequired()])


class Company_add_form(FlaskForm):
    """

    """
    symbol = StringField('symbol', validators=[DataRequired()])
    company_name = StringField('company name', validators=[DataRequired()])


class Portfolio_add_form(FlaskForm):
    """

    """
    portfolio_name = StringField('portfolio_name', validators=[DataRequired()])
