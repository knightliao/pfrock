#!/usr/bin/env python
# coding=utf8
import logging
import os

from tornado import gen
from tornado.web import StaticFileHandler

logger = logging.getLogger('pfrock.static')


class FrockStaticFileHandler(StaticFileHandler):
    def initialize(self, path, default_filename=None):
        self.dir_name, self.file_name = os.path.split(path)
        super(FrockStaticFileHandler, self).initialize(self.dir_name)

    @gen.coroutine
    def get(self, path=None, include_body=True):
        # Ignore 'path'.
        super(FrockStaticFileHandler, self).get(self.file_name, include_body)

    @staticmethod
    def get_handler(url, options):
        file_path = options['file'] if 'file' in options else ""
        path = options['path'] if 'path' in options else ""

        if file_path and path:
            real_url = url[0:url.rfind('/') + 1] + path
            handler = (real_url, FrockStaticFileHandler, {"path": file_path})
            return handler

        if file_path:
            handler = (url, FrockStaticFileHandler, {"path": file_path})
            return handler

        return None
