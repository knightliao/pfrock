#!/usr/bin/env python
# coding=utf8
import logging

from tornado.web import StaticFileHandler

logger = logging.getLogger('pfrock.static')


class FrockStaticDirHandler(StaticFileHandler):
    pass

    @staticmethod
    def get_handler(url, options):
        dir_path = options['dir'] if 'dir' in options else ""
        if dir_path:
            handler = (url, FrockStaticDirHandler, {"path": dir_path})
            return handler
        return None
