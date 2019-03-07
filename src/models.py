from datetime import datetime as dt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from . import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Company(db.Model):
    """

    """
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.ForeignKey('portfolios.id'), nullable=False)
    company_name = db.Column(db.String(256), index=True)
    symbol = db.Column(db.String(12), index=True, unique=True)
    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<Company {}-{}>'.format(self.company_name, self.id)


class Portfolio(db.Model):
    """

    """
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True)
    portfolio_name = db.Column(db.String(256), index=True)
    companies = db.relationship('Company', backref='portfolio', lazy=True)
    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<Portfolio {}>'.format(self.portfolio_name)
