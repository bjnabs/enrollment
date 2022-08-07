import functools
from os import abort
from flask import ( Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from .forms import LoginForm, RegisterForm, OpenIDForm
from .models import db, User 
from . import oid
from flask_login import login_user, logout_user, login_required
from app import auth
#from  ..  import get_db

auth = Blueprint('auth', __name__, template_folder='../templates/auth', url_prefix='/auth')

# signin or login
@auth.route('/signin', methods=('GET', 'POST'))
@auth.route('/login', methods=('GET', 'POST'))
@oid.loginhandler
def signin():
    form = LoginForm()
    openid_form = OpenIDForm()

    if openid_form.validate_on_submit():
        return oid.try_login(
            openid_form.openid.data,
            ask_for=['nickname', 'email'],
            ask_for_optional=['fullname']
        )


    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash( "Logged in successfully.", category='success')
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for("main.index")
            return redirect(next)
        flash('Invalid email or password')
    render_template('auth/signin.html', form=form, openid_form=openid_form)
    
    
    openid_errors = oid.fetch_error()
    if openid_errors:
        flash(openid_errors, category="danger")
    return render_template("auth/signin.html", form = form, openid_form = openid_form)

#register user account
@auth.route('/register', methods=('GET', 'POST'))
@auth.route('/signup', methods=('GET', 'POST'))
@oid.loginhandler
def signup():
    # load the registration form
    form = RegisterForm()
    openid_form = OpenIDForm()
    # validate credentials
    if openid_form.validate_on_submit():
        return oid.try_login(
            openid_form.openid.data, 
            ask_for=['nickname','email'],
            ask_for_optional=['fullname']
        )

    if form.validate_on_submit():
        new_user = User(username = form.username.data,
                        email = form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()

        flash('You have successfully registered', category='success')
        return redirect(url_for('auth.login'))

    openid_errors = oid.fetch_error()
    if openid_errors:
        flash(openid_errors, category="danger")

    return render_template("auth/signup.html", form=form, openid_form=openid_form)

""""
@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

"""


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", category="success")
    return redirect(url_for('main.index'))



def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
