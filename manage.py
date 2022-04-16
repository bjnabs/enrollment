import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand 
from app import db, migrate, create_app
from app.blog.models import Tag, Post 
from app.auth.models import User


env = os.environ.get('APP_ENV', 'dev')
app = create_app('config.%Config' % env.capitalize())


@app.shell_context_processor()
def make_shell_context():
    return dict(app=app, 
                db=db, 
                User=User, 
                Post=Post, 
                Tag=Tag, 
                migrate=migrate)
