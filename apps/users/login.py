from io import BytesIO

from flask import make_response
from marshmallow import ValidationError

from apps.base import BaseHandler
from apps.decorator import is_login
from apps.users.serializers import UserSerializers, UserLoginSerializers
from config import SECRET_KEY, DEBUG
from database.redis_cli import session_redis
from models import User
from utils.tools import get_md5, generate_rand_id, session_handler
from utils.verification_code import gen_verification_code, save_verification_code, check_verification_code


class VerificationCodeHandler(BaseHandler):
    def get(self):
        image, code = gen_verification_code()
        buf = BytesIO()
        image.save(buf, 'png')
        buf_str = buf.getvalue()
        response = make_response(buf_str)
        # response.headers['Content-Type'] = 'application/octet-stream'
        response.headers['Content-Type'] = 'image/png'
        save_verification_code(self.session.sid, code)
        return response


class LoginHandler(BaseHandler):
    def post(self):
        data = self.request.form
        user_login = UserLoginSerializers(context={'self': self})
        try:
            data = user_login.load(data)
        except ValidationError as err:
            return self.write_response("", 0, err.messages)
        login_user = User.query.filter_by(username=data['username'],
                                          password=get_md5(data['password'] + SECRET_KEY)).first()
        if not login_user:
            return self.write_response("", 0, "账号密码错误")
        login_username = login_user.username
        if not DEBUG:
            session_handler(login_username)  # 如果已经登录，则删除之前的session
        token = generate_rand_id()
        self.set_session('uid', login_user.id)
        self.set_session('username', login_username)
        self.set_session('token', token)
        return self.write_response({'token': token})


class LogoutHandler(BaseHandler):
    @is_login
    def post(self):
        self.session.clear()
        return self.write_response('')


class UserInfoHandler(BaseHandler):
    @is_login
    def get(self):
        user = User.query.first()
        user_schema = UserSerializers()
        data = user_schema.dump(user)
        return self.write_response(data)
