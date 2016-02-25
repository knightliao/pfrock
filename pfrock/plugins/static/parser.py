#!/usr/bin/env python
# coding=utf8
from pfrock.core.constants import ROUTER, ROUTER_STATIC_FILE, ROUTER_STATIC_DIR
from pfrock.plugins.static import FrockStaticDirHandler, FrockStaticFileHandler

STATIC_HANDLER_MAP = {
    ROUTER_STATIC_DIR: FrockStaticDirHandler.get_handler,
    ROUTER_STATIC_FILE: FrockStaticFileHandler.get_handler,
}


class StaticHandlerParser(object):
    @staticmethod
    def do(path, methods, options):

        handler_list = []
        if ROUTER in options:
            for route in options[ROUTER]:
                handler = StaticHandlerParser._parser_one(path, methods, route)
                if handler:
                    handler_list.append(handler)
        else:
            handler = StaticHandlerParser._parser_one(path, methods, options)
            if handler:
                handler_list.append(handler)

        return handler_list

    @staticmethod
    def _parser_one(url_path, methods, options):

        for handler_type in STATIC_HANDLER_MAP:
            if handler_type in options:
                return STATIC_HANDLER_MAP[handler_type](url_path, methods, options)

        return None
