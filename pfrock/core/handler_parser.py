#!/usr/bin/env python
# coding=utf8
from pfrock.core import logger
from pfrock.plugins.handler.parser import HandlerParser
from pfrock.plugins.proxy.parser import ProxyHandlerParser
from pfrock.plugins.static.parser import StaticHandlerParser

HANDLER_MAP = {
    'pfrock-proxy': ProxyHandlerParser.do,
    'pfrock-static': StaticHandlerParser.do,
    'other': HandlerParser.do
}


class HandlerParser(object):
    @classmethod
    def get_handlers(cls, config_server):
        routes = config_server.routes

        handler_list = []
        for route in routes:

            def add_handler(handler):
                if handler:
                    logger.debug("add : " + str(handler))
                    handler_list.append(handler)

            if route.handler in HANDLER_MAP:
                handlers = HANDLER_MAP[route.handler](route.path, route.methods, route.options)

                if type(handlers) == list:
                    for handler in handlers:
                        add_handler(handler)
                else:
                    add_handler(handlers)
            else:
                handler = HANDLER_MAP['other'](route.path, route.methods, route.handler, route.options)
                add_handler(handler)

        return handler_list
