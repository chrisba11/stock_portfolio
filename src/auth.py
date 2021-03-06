import functools
from flask import render_template, flash, redirect, url_for, session, abort, g
from . import app
from .forms import AuthForm
from .models import db, User


def login_required(view):
    """
    Function to wrap a view or something like that. No idea what it means.
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
    Function to load the information for the logged in user, if one is logged in.
    """
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    GET & POST routes for the '/register' path. GET will render the register page,
    POST will register the user and save them to the DB and then render '/login' page.
    """
    form = AuthForm()

    if form.validate_on_submit():
        email = form.data['email']
        password = form.data['password']
        error = None

        if not email or not password:
            error = 'Invalid email or password'

        if User.query.filter_by(email=email).first() is not None:
            flash('{} has already been registered!'.format(email))

            return redirect(url_for('.login'))

        if error is None:
            user = User(email=email, raw_password=password)
            db.session.add(user)
            db.session.commit()

            flash('Registration complete. Please log in.')

            return redirect(url_for('.login'))

        flash(error)

    return render_template('auth/register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    GET & POST routes for the '/login' page. GET will render the page so the user can log in,
    POST will log the user in, if they provide valid input, and render their portfolio page.
    """
    form = AuthForm()

    if form.validate_on_submit():
        email = form.data['email']
        password = form.data['password']
        error = None

        user = User.query.filter_by(email=email).first()

        if user is None or not User.check_password_hash(user, password):
            error = 'Invalid username or password.'

        if error is None:
            session.clear()
            session['user_id'] = user.id

            return redirect(url_for('.company_detail'))

        flash(error)

    return render_template('auth/login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    """
    GET route to the '/logout' page to log the user out of the application.
    """
    session.clear()
    flash('See you again soon!')

    return redirect(url_for('.login'))
