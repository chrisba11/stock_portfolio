import functools
from flask import render_template, flash, redirect, url_for, session, abort, g
from . import app
from .forms import AuthForm
from .models import db, User


def login_required(view):
    """

    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            abort(404)

        return view(**kwargs)

    return wrapped_view


@app.before_request
def load_logged_in_user():
    """

    """
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@app.route('/register', methods=['GET', 'POST'])
