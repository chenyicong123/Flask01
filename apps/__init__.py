from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_session import Session

from apps.urls import register_urls
from models import db

__all__ = ['create_app']


def init_session(app):
    sess = Session()
    sess.init_app(app)


def init_migrate(app):
    migrate = Migrate(compare_type=True)
    # migrate = Migrate()
    db.init_app(app)
    migrate.init_app(app, db)


def init_cors(app):
    CORS(app)


def init_urls(app):
    register_urls(app)


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    init_migrate(app)
    init_session(app)
    init_cors(app)
    init_urls(app)
    return app
