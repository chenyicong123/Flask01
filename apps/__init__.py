from flask import Flask

__all__ = ['create_app']


def create_app():
    app = Flask(__name__)

    return app
