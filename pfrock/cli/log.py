#!/usr/bin/env python
# coding=utf8
from logging.config import dictConfig


def make_logging(debug_mode=False):
    logging_level = "INFO"
    if debug_mode:
        logging_level = "DEBUG"

    logging_config = {

        'version': 1,
        'formatters': {
            'verbose': {
                'format': '[%(levelname)1.1s %(asctime)s %(name)s %(threadName)s %(module)s:%(lineno)d] %(message)s'
            },
            'simple': {
                'format': '[%(levelname)1.1s %(asctime)s %(name)s %(threadName)s %(module)s:%(lineno)d] %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            }
        },
        'loggers': {
            'root': {'level': logging_level, 'handlers': ['console']},
            'tornado': {'level': logging_level, 'handlers': ['console']},
            'pfrock': {'level': logging_level, 'handlers': ['console']},
        }
    }

    dictConfig(logging_config)
