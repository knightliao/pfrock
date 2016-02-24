#!/usr/bin/env python
# coding=utf8
import logging

import tornado.autoreload
import tornado.ioloop
import tornado.web

logger = logging.getLogger('pfrock2.core')


class PFrock(object):
    def __init__(self, auto_reload=True, port=8888):
        self.app = tornado.web.Application(autoreload=True)
        self.auto_reload = auto_reload
        self.port = port
        logger.info("started server " + str(port) + (" with autoreload mode" if self.auto_reload else ""))

    def add_handler(self, handlers):
        self.app.add_handlers(".*$", handlers)

    def start(self):
        self.app.listen(8888)
        tornado.ioloop.IOLoop.current().start()

    def add_watch(self, watch_file):
        tornado.autoreload.watch(watch_file)
