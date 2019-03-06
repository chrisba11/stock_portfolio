from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from . import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(256), index=True, unique=True)
    symbol = db.Column(db.String(12), index=True, unique=True)

    def __repr__(self):
        return '<Company {}-{}>'.format(self.company_name, self.id)
