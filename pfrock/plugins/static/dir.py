#!/usr/bin/env python
# coding=utf8

from tornado.web import StaticFileHandler

from pfrock.core.constants import ROUTER_METHOD, ROUTER_PATH, ROUTER_STATIC_DIR


class FrockStaticDirHandler(StaticFileHandler):
    def initialize(self, path, default_filename=None, **kwargs):
        self.root = path
        self.default_filename = default_filename

    def post(self):
        return self.get()

    def delete(self):
        return self.get()

    def put(self):
        return self.get()

    @staticmethod
    def get_handler(url, methods, options):
        dir_path = options[ROUTER_STATIC_DIR] if ROUTER_STATIC_DIR in options else ""
        if dir_path:
            handler = (url, FrockStaticDirHandler, {ROUTER_PATH: dir_path, ROUTER_METHOD: methods})
            return handler
        return None
