from flask import Flask
from flask_migrate import Migrate

from models import db

__all__ = ['create_app']


def init_migrate(app):
    migrate = Migrate(compare_type=True)
    # migrate = Migrate()
    db.init_app(app)
    migrate.init_app(app, db)


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    init_migrate(app)

    return app
