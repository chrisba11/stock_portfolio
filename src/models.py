from datetime import datetime as dt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from passlib.hash import sha256_crypt
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
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    portfolio_name = db.Column(db.String(256), index=True)
    companies = db.relationship('Company', backref='portfolio', lazy=True)
    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<Portfolio {}>'.format(self.portfolio_name)


class User(db.Model):
    """

    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), index=True, unique=True, nullable=False)
    pass_hash = db.Column(db.String(256), nullable=False)
    portfolios = db.relationship('Portfolio', backref='user', lazy=True)
    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<User {}>'.format(self.email)

    def __init__(self, email, raw_password):
        self.email = email
        self.pass_hash = sha256_crypt.hash(raw_password)

    @classmethod
    def check_password_hash(cls, user, password):
        """

        """
        if user is not None:
            if sha256_crypt.verify(password, user.pass_hash):
                return True

        return False
