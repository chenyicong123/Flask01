# coding: utf-8
import functools


def is_login(func):
    """
    登录认证的装饰器，从请求头获取X-Token和session中存储用户token比较
    """
    def wrapper(self, *args, **kwargs):
        user_id = self.user_id
        if user_id is None:
            return self.write_response('', 0, '用户未登录', http_status=401)
        token = self.get_session('token')
        if token and self.request.headers.get('X-Token') == token:
            return func(self, *args, **kwargs)
        else:
            return self.write_response('', 0, '登录认证失败', http_status=401)
    return wrapper
