#!/usr/bin/env python
# coding=utf8
import traceback

from pfrock2.plugins.handler import import_from_file, logger

KEY_URL = 'url'
KEY_HOST = 'host'


class HandlerParser(object):
    @staticmethod
    def do(path, handler_module_path, options):

        try:
            my_class = import_from_file(handler_module_path)
            handler = (path, my_class, options)
            return handler
        except:
            logger.error(traceback.format_exc())
            return None
