import logging.config

from config import DEBUG_LOG_FILE, ERROR_LOG_FILE

__all__ = ['get_logger']

standard_format = '[%(levelname)s] - [%(asctime)s] [%(filename)s:%(funcName)s][line:%(lineno)d]: %(message)s'


# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format,
            "datefmt": '%Y-%m-%d %H:%M:%S'
        }
    },
    'filters': {},
    'handlers': {
        # 打印到文件的日志,收集操作日志
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': DEBUG_LOG_FILE,
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
            'encoding': 'utf-8',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': ERROR_LOG_FILE,
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 5,
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'debug': {
            'handlers': ['debug'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'error': {
            'handlers': ['error'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置


def get_logger():

    logger = logging.getLogger()
    setattr(logger, 'debug', logging.getLogger('debug').debug)
    setattr(logger, 'error', logging.getLogger('error').error)
    return logger


logger = get_logger()


