# coding: utf-8
import os
from redis import StrictRedis

try:
    from local_config import *
except:
    pass

# 日志
PATH = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(PATH, 'logs')
if not os.path.isdir(LOG_PATH):
    os.mkdir(LOG_PATH)

ERROR_LOG_FILE = os.path.join(LOG_PATH, 'error.log')
DEBUG_LOG_FILE = os.path.join(LOG_PATH, 'debug.log')

HOST = '0.0.0.0'
PORT = 9000
DEBUG = False

SECRET_KEY = 'chenyicong'
SECRET_KEY_DES = '12345678'
SESSION_USE_SIGNER = True
SESSION_TYPE = 'redis'
PERMANENT_SESSION_LIFETIME = 3600  # 失效时间(秒)
SQLALCHEMY_TRACK_MODIFICATIONS = False

DATABASE = {
    'host': '127.0.0.1',
    'port': 3306,
    'username': 'root',
    'password': '123456',
    'db': 'flask01',
}

REDIS_CONFIG = {
    'host': '127.0.0.1',
    'port': '6379',
    'password': '',
    'db': 10,
    'code_db': 9,  # 验证码
}

# 邮件设置
SMTP_HOST = 'smtp.mxhichina.com'
SMTP_PORT = 465
SMTP_USE_SSL = True
SMTP_USER = ''
SMTP_PASSWORD = ''

SESSION_REDIS = StrictRedis(host=REDIS_CONFIG["host"], port=REDIS_CONFIG["port"], db=REDIS_CONFIG["db"],
                            password=REDIS_CONFIG["password"], socket_connect_timeout=2, charset='utf-8')

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(DATABASE['username'],
#                                                                   DATABASE['password'],
#                                                                   DATABASE['host'],
#                                                                   DATABASE['port'],
#                                                                   DATABASE['db'])

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(DATABASE['username'],
                                                                         DATABASE['password'],
                                                                         DATABASE['host'],
                                                                         DATABASE['port'],
                                                                         DATABASE['db'])
VERIFICATION_CODE_EXPIRE = 60  # 验证码过期时间
