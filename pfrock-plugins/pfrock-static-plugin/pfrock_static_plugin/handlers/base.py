# !/usr/bin/env python
# coding=utf8
from tornado.web import StaticFileHandler, os

from pfrock_static_plugin.handlers import ROUTER_HEADER


class FrockStaticBaseHandler(StaticFileHandler):
    def initialize(self, path, default_filename=None, **kwargs):
        self.my_headers = kwargs.get(ROUTER_HEADER)

        super(FrockStaticBaseHandler, self).initialize(path, default_filename)

    def set_headers(self):

        # sys guess
        super(FrockStaticBaseHandler, self).set_headers()

        # guess by extension
        filename, file_extension = os.path.splitext(self.path)
        if file_extension == ".json":
            self.set_header("Content-Type", 'application/json')

        # user specify
        if self.my_headers:
            for key in self.my_headers:
                self.set_header(key, self.my_headers[key])
