
import os
import warnings
from datetime import datetime
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__)) 

class Config(object):
    DEBUG = False
    TESTING = False
    DEVELOPMENT = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY", "736670cb10a600b695a55839ca3a5aa54a7d7356cdef815d2ad6e19a2031182b")
    RECAPTCHA_PUBLIC_KEY = "6LdKkQQTAAAAAEH0GFj7NLg5tGicaoOus7G9Q5Uw"
    RECAPTCHA_PRIVATE_KEY = '6LdKkQQTAAAAAMYroksPTJ7pWhobYb88fTAcxcYn'
    POSTS_PER_PAGE = 10

    TWITTER_API_KEY = "XXXX"
    TWITTER_API_SECRET = "XXXX"
    FACEBOOK_CLIENT_ID = "XXX"
    FACEBOOK_CLIENT_SECRET = "XXXX"

    MONGODB_SETTINGS = {'db':'UTA_Enrollment',
                        'host': 'mongodb://localhost:27017/UTA_Enrollment', 
                        'port': 27017
                        }
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:N%40b%242107@localhost:5432/wordcount"
    SQLALCHEMY_ENGINE_OPTIONS = "postgresql+psycopg2://postgres:N%40b%242107@localhost:5432/wordcount"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    #SQLALCHEMY_BINDS = {}
    #SQLALCHEMY_RECORD_QUERIES
    #SQLALCHEMY_NATIVE_UNICODE
    #SQLALCHEMY_POOL_SIZE
    #SQLALCHEMY_POOL_TIMEOUT
    #SQLALCHEMY_POOL_RECYCLE
    #SQLALCHEMY_MAX_OVERFLOW

    #cookies
    #REMEMBER_COOKIE_NAME
    #REMEMBER_COOKIE_DURATION
    #REMEMBER_COOKIE_DOMAIN
    #REMEMBER_COOKIE_PATH
    #REMEMBER_COOKIE_SECURE
    #REMEMBER_COOKIE_HTTPONLY
    #REMEMBER_COOKIE_REFRESH_EACH_REQUEST
    #REMEMBER_COOKIE_SAMESITE

    #session
    SESSION_PROTECTION = "strong"




class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
