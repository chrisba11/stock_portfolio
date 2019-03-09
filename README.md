# stock_portfolio

**Author**: Chris Ball
**Version**: 1.6.3

## Overview
This is a flask app that allows a user to search for companies by stock symbol and save them to the database with a portfolio name associated with each company. They will have to register and log in to use the search and save functionality. When the app renders their saved companies, all companies within a portfolio will be listed together.

## Getting Started
To use this application, you will want to clone the repo, open a virtual environment with pipenv, and run a pipenv install to download the dependencies. From there, you will need to create a database using the `flask db init` command, followed by `flask db migrate` and `flask db upgrade`. Then you will be able to start the server with `flask run`. At that point, you can navigate to http://localhost:4000 and you should see the welcome page.

## Architecture
This app utilizies the Flask framework, along with requests, flask-sqlalchemy, "psycopg2-binary", flask-migrate, flask-wtf, passlib, and gunicorn. Testing is being performed using pytest.

I am using jinja2 templating for server side rendering of HTML.

## API


[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
flask = "*"
requests = "*"
flask-sqlalchemy = "*"
"psycopg2-binary" = "*"
flask-migrate = "*"
python-dotenv = "*"
flask-wtf = "*"
gunicorn = "*"
passlib = "*"

[dev-packages]
pytest = "*"
pep8 = "*"

[requires]
python_version = "3.7"
