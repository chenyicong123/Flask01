# coding: utf-8
import pickle
import random
import string
import time
from _md5 import md5

from database.redis_cli import session_redis


def get_md5(_str):
    """

    :param _str:
    :return:
    """
    return md5(str(_str).encode("utf-8")).hexdigest()


def generate_rand_id(_str=None):
    ti = int(time.time())
    if not _str:
        _str = list(string.ascii_letters + string.digits)
        random.shuffle(_str)
        _str = ''.join(_str)
    rand = str(random.randint(0, 99999))
    res = str(ti) + _str + rand
    res = res.encode("utf-8")
    res = md5(res).hexdigest()
    return res


def session_handler(name):
    """
    处理同一用户登录
    :param name:用户名
    :return:
    """
    keys = session_redis.keys()
    for key in keys:
        data = session_redis.get(key)
        data_dict = pickle.loads(data)
        if data_dict.get('username') == name:
            session_redis.delete(key)
