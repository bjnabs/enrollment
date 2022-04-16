import os
from flask import Flask, render_template  
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  
from flask_ckeditor import CKEditor


#api = Api()
#database engines
#db = MongoEngine()
db = SQLAlchemy()
migrate = Migrate()
ckeditor = CKEditor() 


def page_not_found(error):
    return render_template('page404.html'), 404


def create_app(Config): 
    app = Flask(__name__) 
    env_config = os.getenv("APP_ENV", "config.DevelopmentConfig")
    app.config.from_object(env_config)
    

    db.init_app(app)
    migrate.init_app(app, db)  
    ckeditor.init_app(app)
    #api.init_app(app)

    from .auth import create_module as auth_create_module
    from .blog import create_module as blog_create_module
    from .courses import create_module as courses_create_module
    from .projects import create_module as projects_create_module
    from .main import create_module as main_create_module

    auth_create_module(app)
    blog_create_module(app)
    courses_create_module(app)
    projects_create_module(app)
    main_create_module(app)
 
    
    app.register_error_handler(404, page_not_found)
    return app

