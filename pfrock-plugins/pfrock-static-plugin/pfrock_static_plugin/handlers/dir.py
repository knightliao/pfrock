#!/usr/bin/env python
# coding=utf8

from pfrock_static_plugin.handlers import ROUTER_STATIC_DIR, ROUTER_PATH
from pfrock_static_plugin.handlers.base import FrockStaticBaseHandler


class FrockStaticDirHandler(FrockStaticBaseHandler):
    def initialize(self, path, default_filename=None, **kwargs):
        super(FrockStaticDirHandler, self).initialize(path, default_filename, **kwargs)

    def post(self):
        return self.get()

    def delete(self):
        return self.get()

    def put(self):
        return self.get()

    @staticmethod
    def get_handler(url, options):
        dir_path = options[ROUTER_STATIC_DIR] if ROUTER_STATIC_DIR in options else ""
        if dir_path:
            handler = (url, FrockStaticDirHandler, {ROUTER_PATH: dir_path})
            return handler
        return None
