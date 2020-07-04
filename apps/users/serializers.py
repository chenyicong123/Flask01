from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError, validates

from models import User
from utils.verification_code import check_verification_code

ma = Marshmallow()


class UserSerializers(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ('username',)


class UserLoginSerializers(ma.Schema):
    username = fields.String(required=True, error_messages={"required": "用户名称不能为空"})
    password = fields.String(required=True, error_messages={"required": "密码不能为空"})
    code = fields.String(required=True, error_messages={"required": "验证码不能为空"})

    @validates('password')
    def validate_password(self, password):
        if len(password) < 6:
            raise ValidationError("密码长度小于6位")

    @validates('code')
    def validate_code(self, code):
        status, msg = check_verification_code(self.context['self'].session.sid, code)
        # if not status:
        #     raise ValidationError(msg)
