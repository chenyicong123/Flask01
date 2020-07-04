import json

from flask import make_response, request, session
from flask.views import MethodView

from utils.logger import logger
from models import db


class BaseHandler(MethodView):
    """
    Flask Application BaseHandler
    """

    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__()
        self.request = request
        self.session = session
        self.logger = logger
        self.db = db

    def set_session(self, key, value):
        self.session[key] = value

    def get_session(self, key):
        return self.session.get(key, None)

    def del_session(self, key):
        return self.session.pop(key, None)

    def clear_session(self):
        self.session.clear()

    @property
    def user_id(self):
        return self.session.get('uid', None)

    @staticmethod
    def write_response(data=None, status=1, error_msg="", http_status=200):
        if data is None:
            data = {}

        _data = {
            "data": data,
            "status": status,
            "message": error_msg,
        }
        _data = json.dumps(_data)
        response = make_response(_data, http_status)
        response.headers['Content-Type'] = 'application/json'
        origin = request.headers.get("Origin")
        response.headers['Access-Control-Allow-Origin'] = origin
        return response

    @staticmethod
    def options(*args, **kwargs):
        origin = request.headers.get("Origin")
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = origin
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, Content-Type, accept'
        return response
