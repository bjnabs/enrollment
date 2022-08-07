from flask import g
from psycopg2_connect import connect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql+psycopg2://postgres:N%40b%242107@localhost:5432/wordcount", echo=True, encoding='UTF-8')

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import app.main.models
    Base.metadata.create_all(bind=engine)


def get_db():
    if 'db' not in g:
        g.db = connect( 
            dbname="wordcount", 
            user="postgres", 
            password="N@b$2107",
            host = 'localhost', 
            port=5432)

    return g.db
