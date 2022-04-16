
import base64
import functools
from flask import flash, redirect, url_for, session, abort, request
from http import HTTPStatus
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user, login_user, AnonymousUserMixin
from flask_openid import OpenID
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
from flask_dance.contrib.linkedin import make_linkedin_blueprint, linkedin
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer import oauth_authorized

bcrypt = Bcrypt()
oid = OpenID()

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page resources"
login_manager.login_message_category = "info"
login_manager.refresh_view = "auth.login"
login_manager.needs_refresh_message = ( u"To protect your account, please reauthenticate to access this page." )
login_manager.needs_refresh_message_category = "info"
login_manager.session_protection = "strong"

@login_manager.user_loader
def load_user(userid):
    from models import User
    return User.query.get(userid)


@login_manager.unauthorized_handler
def unauthorized():
    if request.blueprint == 'api':
        abort(HTTPStatus.UNAUTHORIZED)
    return redirect(url_for('auth.login'))


"""
@login_manager.request_loader
def load_user_from_request(request):

    # first, try to login using the api_key url arg
    api_key = request.args.get('api_key')
    if api_key:
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # next, try to login using Basic Auth
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        try:
            api_key = base64.b64decode(api_key)
        except TypeError:
            pass
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # finally, return None if both methods did not login the user
    return None
    """


def create_module(app, **kwargs):
    bcrypt.init_app(app)
    login_manager.init_app(app)
    from .controllers import auth
    app.register_blueprint(auth)



class UserAnonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'
    
    @property
    def is_authenticated(self):
        return False

    @property
    def is_active(self):
        return False

    @property
    def is_anonymous(self):
        return True

    def get_id(self):
        return
