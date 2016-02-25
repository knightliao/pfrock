#!/usr/bin/env python
# coding=utf8
import traceback

from pfrock.core.constants import ROUTER_METHOD
from pfrock.plugins.handler import import_from_file, logger

KEY_URL = 'url'
KEY_HOST = 'host'


class HandlerParser(object):
    @staticmethod
    def do(path, methods, handler_module_path, options):

        if not options:
            options = {}
        options[ROUTER_METHOD] = methods

        try:
            my_class = import_from_file(handler_module_path)
            handler = (path, my_class, options)
            return handler
        except:
            logger.error(traceback.format_exc())
            return None
