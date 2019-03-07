from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from .models import Portfolio


class Company_form(FlaskForm):
    """

    """
    symbol = StringField('symbol', validators=[DataRequired()])


class Company_add_form(FlaskForm):
    """

    """
    symbol = StringField('symbol', validators=[DataRequired()])
    company_name = StringField('company name', validators=[DataRequired()])
    portfolios = SelectField('portfolios')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.portfolios.choices = [(str(p.id), p.portfolio_name) for p in Portfolio.query.all()]


class Portfolio_add_form(FlaskForm):
    """

    """
    portfolio_name = StringField('Portfolio Name', validators=[DataRequired()])
