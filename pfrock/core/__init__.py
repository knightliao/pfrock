#!/usr/bin/env python
# coding=utf8
import logging

import tornado.autoreload
import tornado.ioloop
import tornado.web

from pfrock.core.web import MyApplication

logger = logging.getLogger('pfrock.core')


class PFrock(object):
    def __init__(self, auto_reload=True, port=8888):
        self.app = MyApplication(autoreload=True)
        self.auto_reload = auto_reload
        self.port = port
        logger.info("started server " + str(port) + (" with autoreload mode" if self.auto_reload else ""))

    def add_handler(self, handlers):
        self.app.add_handlers(".*$", handlers)

    def start(self):
        self.app.listen(self.port)
        tornado.ioloop.IOLoop.current().start()

    def add_watch(self, watch_file):
        tornado.autoreload.watch(watch_file)
