# !/usr/bin/env python
# coding=utf8
import json
import traceback

from tornado.web import RequestHandler

from pfrock.cli import logger
from pfrock.core.constants import PFROCK_CONFIG_SERVER, PFROCK_CONFIG_ROUTER, PFROCK_CONFIG_PORT, ROUTER_METHOD, \
    ROUTER_PATH, ROUTER_OPTIONS, ROUTER_HANDLER
from pfrock.core.lib import auto_str


@auto_str
class PfrockConfigRouter(object):
    SUPPORTED_METHODS = RequestHandler.SUPPORTED_METHODS

    def __init__(self, path, methods, handler, options={}):
        self.path = path
        self.handler = handler
        self.options = options
        self.methods = []

        if methods == "any":
            self.methods = []
        else:
            for method in methods:
                method = method.upper()
                if method in self.SUPPORTED_METHODS:
                    self.methods.append(method)


@auto_str
class PfrockConfigServer(object):
    def __init__(self, routes, port):
        self.routes = routes
        self.port = port


class PfrockConfigParser(object):
    @classmethod
    def _parse_router(cls, router):
        path = router[ROUTER_PATH] if ROUTER_PATH in router else None
        methods = router[ROUTER_METHOD] if ROUTER_METHOD in router else []
        handler = router[ROUTER_HANDLER] if ROUTER_HANDLER in router else None
        options = router[ROUTER_OPTIONS] if ROUTER_OPTIONS in router else None
        if path and handler:
            return PfrockConfigRouter(path, methods, handler, options)
        return None

    @classmethod
    def _parse_routers(cls, routers):
        router_list = []
        for router in routers:
            router = cls._parse_router(router)
            if router:
                router_list.append(router)
        return router_list

    @classmethod
    def _parse_servers(cls, server):
        port = server[PFROCK_CONFIG_PORT] if PFROCK_CONFIG_PORT in server else None
        routers = cls._parse_routers(server[PFROCK_CONFIG_ROUTER]) if PFROCK_CONFIG_ROUTER in server else None
        if port and routers:
            return PfrockConfigServer(routers, port)

    @classmethod
    def do(cls, config_file_path):
        with open(config_file_path, 'r') as fin:

            try:
                config_data = json.load(fin)
            except:
                logger.error("%s not well formed \n%s" % (config_file_path, traceback.format_exc()))
                return None

            config_servers = config_data[PFROCK_CONFIG_SERVER] if PFROCK_CONFIG_SERVER in config_data else None
            if config_servers:
                for config_server in config_servers:
                    config_server = cls._parse_servers(config_server)
                    # todo: dev version just support one server
                    return config_server
            return None
