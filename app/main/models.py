from email.policy import default
from app import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSON
from datetime import date, datetime


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)



class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    addresses = db.relationship('Address', backref='person', lazy=True)



class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
                          nullable=False)

class Crimes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    latitude = db.Column(db.Float, nullable = False)
    longitude = db.Column(db.Float, nullable=False)
    date_created = db.Column(datetime, default = datetime.now, nullable=False)
    category = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    date_updated = db.Column(datetime, default = datetime.now, nullable=False)
