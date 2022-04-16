from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin, SQLAlchemyStorage
from datetime import datetime, timedelta
from . import bcrypt, AnonymousUserMixin
from .. import db  

db = SQLAlchemy()

roles = db.Table(
    'role_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)



class User(db.Model):  
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)  
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255),  nullable=False, index=True, unique=True)
    password = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default = datetime.now)  
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    
    def __init__(self, username):    
        self.username = username  
    
    
    def __repr__(self):    
        return "<User '{}'>".format(self.username)


    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


    @property
    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return self.is_active

    
    @property 
    def is_active(self): 
        return True


    
    @property
    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False


    def get_id(self):
        try:
            return str(self.id)
        except AttributeError:
            raise NotImplementedError("No `id` attribute - override `get_id`") from None


class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)


# get_current_user() is a function that returns the current logged in user
#blueprint.storage = SQLAlchemyStorage(OAuth, db.session, user=get_current_user)
