# coding: utf-8

from redis import StrictRedis

from config import REDIS_CONFIG


def conn_redis(database=REDIS_CONFIG['db']):
    """
    redis 连接
    """
    cli = StrictRedis(host=REDIS_CONFIG["host"],
                      port=REDIS_CONFIG["port"],
                      db=database,
                      password=REDIS_CONFIG["password"],
                      socket_connect_timeout=2,
                      charset='utf-8')
    return cli


session_redis = conn_redis()  # session
code_redis = conn_redis(database=REDIS_CONFIG['code_db'])  # 验证码
