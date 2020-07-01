from models import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, doc="主键", comment="主键")
    username = db.Column(db.String(64), nullable=False, index=True, doc="用户名称", comment="用户名称")
    password = db.Column(db.String(128), nullable=False, doc="密码", comment="密码")
    ban = db.Column(db.Boolean, index=True, default=False, doc="是否禁用", comment="是否禁用")

    def __repr__(self):
        return '<User %r>' % self.id
