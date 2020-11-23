import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate


database_name = 'heroku_test'
user_name = 'postgres'
user_password = 'w1zu'
host = 'localhost:5432'
database_path = "postgres://{}:{}@{}/{}".format(user_name, user_password, host, database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    # for local database use the variable database_path with your database URI
    #app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://wqlwqncscphcfx:3e859ca1b5ec222029233138067b706303f74ac2c287d2a1d892bb086f8156ab@ec2-54-163-47-62.compute-1.amazonaws.com:5432/dvfahj6moq3cs'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    migrate = Migrate(app, db)
    db.app = app
    db.init_app(app)
    db.create_all()


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    release_date = db.Column(db.String(120), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }


class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(120), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
