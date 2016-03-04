#!/usr/bin/env python
# coding=utf8
import importlib
import logging
import traceback

from pfrock.core.constants import ROUTER_METHOD
from pfrock.core.plugin import PLUGIN_CLASS_GET_HANDLER
from pfrock.core.register import PfrockPluginRegister

logger = logging.getLogger('pfrock.routes')


class RoutesMgr(object):
    @classmethod
    def _import_route(cls, module_name):

        # import
        try:
            module_class = importlib.import_module(module_name)

            PfrockPluginRegister.register(module_class, module_name)
            return True
        except:
            logger.warn("cannot import plugin handler %s \n %s" % (module_name, traceback.format_exc()))
            return False

    @classmethod
    def _get_http_handler(cls, one_route, register_handler_class):

        try:

            handlers = getattr(register_handler_class(),
                               PLUGIN_CLASS_GET_HANDLER)(one_route.options,
                                                         path=one_route.path,
                                                         methods=one_route.methods)

            real_handlers = []
            if handlers:
                handlers = handlers if type(handlers) == list else [handlers]
                # append methods for handler options
                for handler in handlers:
                    if type(handler) == tuple:
                        real_handler = handler
                    else:
                        real_handler = (one_route.path, handler, one_route.options)

                    real_handler[2][ROUTER_METHOD] = one_route.methods
                    real_handlers.append(real_handler)
                return real_handlers

            return []

        except:
            logger.warn(traceback.format_exc())
            return []

    @classmethod
    def _get_one_route(cls, one_route):

        register_handler_class = PfrockPluginRegister.get_handler(one_route.handler)
        if register_handler_class:
            return cls._get_http_handler(one_route, register_handler_class)
        else:
            return None

    @classmethod
    def get_routes(cls, config_server):
        routes = config_server.routes

        route_list = []
        for route in routes:

            def add_route(route):
                if route:
                    logger.debug("add : %s %s %s " % (route[0], route[1].__name__, route[2]))
                    route_list.append(route)

            if cls._import_route(route.handler):
                cur_routes = cls._get_one_route(route)
                if type(cur_routes) == list:
                    for cur_route in cur_routes:
                        add_route(cur_route)
                else:
                    add_route(cur_routes)

        return route_list
