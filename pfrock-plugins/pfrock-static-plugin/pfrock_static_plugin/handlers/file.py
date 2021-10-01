#!/usr/bin/env python
# coding=utf8
import os

import tornado.gen

from pfrock_static_plugin.handlers import ROUTER_STATIC_FILE, ROUTER_PATH, ROUTER_HEADER
from pfrock_static_plugin.handlers.base import FrockStaticBaseHandler


class FrockStaticFileHandler(FrockStaticBaseHandler):
    def post(self):
        return self.get()

    def delete(self):
        return self.get()

    def put(self):
        return self.get()

    def initialize(self, path, default_filename=None, **kwargs):
        self.dir_name, self.file_name = os.path.split(path)
        super(FrockStaticFileHandler, self).initialize(self.dir_name, **kwargs)

    @tornado.gen.coroutine
    def get(self, path=None, include_body=True):
        # Ignore 'path'.
        try:
            yield super(FrockStaticFileHandler, self).get(self.file_name, include_body)
        except Exception, e:
            # when no found , return 404 just ok
            self.set_status(404)

    def compute_etag(self):
        """Sets the ``Etag`` header based on static url version.

        This allows efficient ``If-None-Match`` checks against cached
        versions, and sends the correct ``Etag`` for a partial response
        (i.e. the same ``Etag`` as the full file).

        .. versionadded:: 3.1
        """
        if not hasattr(self, 'absolute_path'):
            return None
        return super(FrockStaticFileHandler, self).compute_etag()

    @staticmethod
    def get_handler(url, options):

        # path
        file_path = options[ROUTER_STATIC_FILE] if ROUTER_STATIC_FILE in options else ""
        path = options[ROUTER_PATH] if ROUTER_PATH in options else ""

        # header
        headers = options[ROUTER_HEADER] if ROUTER_HEADER in options else {}

        # guess by extension
        filename, file_extension = os.path.splitext(file_path)
        if file_extension == ".json":
            headers["Content-Type"] = 'application/json'

        if file_path and path:
            real_url = url[0:url.rfind('/') + 1] + path
            handler = (real_url, FrockStaticFileHandler, {ROUTER_PATH: file_path, ROUTER_HEADER: headers})
            return handler

        if file_path:
            handler = (url, FrockStaticFileHandler, {ROUTER_PATH: file_path, ROUTER_HEADER: headers})
            return handler

        return None
