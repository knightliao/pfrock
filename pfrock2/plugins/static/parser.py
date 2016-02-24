#!/usr/bin/env python
# coding=utf8
from pfrock2.plugins.static import FrockStaticDirHandler, FrockStaticFileHandler

STATIC_HANDLER_MAP = {
    'dir': FrockStaticDirHandler.get_handler,
    'file': FrockStaticFileHandler.get_handler,
}

KEY_PATH = 'path'


class StaticHandlerParser(object):
    @staticmethod
    def do(path, options):

        handler_list = []
        if "routes" in options:
            for route in options['routes']:
                handler = StaticHandlerParser._parser_one(path, route)
                if handler:
                    handler_list.append(handler)
        else:
            handler = StaticHandlerParser._parser_one(path, options)
            if handler:
                handler_list.append(handler)

        return handler_list

    @staticmethod
    def _parser_one(url_path, options):

        for handler_type in STATIC_HANDLER_MAP:
            if handler_type in options:
                return STATIC_HANDLER_MAP[handler_type](url_path, options)

        return None
