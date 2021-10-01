#!/usr/bin/env python
# coding=utf8

from pfrock_static_plugin.handlers import ROUTER_STATIC_FILE, ROUTER_STATIC_DIR, ROUTER_PATH, ROUTER, ROUTER_HEADER, \
    ROUTER_STATIC_FILES
from pfrock_static_plugin.handlers.dir import FrockStaticDirHandler
from pfrock_static_plugin.handlers.file import FrockStaticFileHandler
from pfrock_static_plugin.handlers.files import FrockStaticFilesHandler

STATIC_HANDLER_MAP = {
    ROUTER_STATIC_DIR: FrockStaticDirHandler.get_handler,
    ROUTER_STATIC_FILE: FrockStaticFileHandler.get_handler,
    ROUTER_STATIC_FILES: FrockStaticFilesHandler.get_handler,
}


class PfrockStaticPlugin(object):
    def get_handler(self, options, **kwargs):
        handler_list = []

        # url path
        url_path = kwargs.get(ROUTER_PATH)

        # nesting config
        if ROUTER in options:

            # parent header setting
            parent_header = options[ROUTER_HEADER] if ROUTER_HEADER in options else {}

            for one_route in options[ROUTER]:

                # copy parent header to child header, child setting first
                copy_header = dict(parent_header)
                if ROUTER_HEADER in one_route:
                    copy_header.update(one_route[ROUTER_HEADER])
                one_route[ROUTER_HEADER] = copy_header

                # get header
                handler = self.__parser_one(url_path, one_route)
                if handler:
                    handler_list.append(handler)
        else:
            handler = self.__parser_one(url_path, options)
            if handler:
                handler_list.append(handler)

        return handler_list

    def __parser_one(self, url_path, options):

        for handler_type in STATIC_HANDLER_MAP:
            if handler_type in options:
                return STATIC_HANDLER_MAP[handler_type](url_path, options)

        return None
