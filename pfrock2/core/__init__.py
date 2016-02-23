#!/usr/bin/env python
# coding=utf8
import tornado.ioloop
import tornado.web


class PFrock(object):
    def __init__(self):
        self.app = None

    def make_app(self, handlers=[]):
        self.app = tornado.web.Application(autoreload=True)
        self.add_handler(handlers)

    def add_handler(self, handlers):
        self.app.add_handlers(".*$", handlers)

    def start_app(self, app):
        self.app.listen(8888)
        tornado.ioloop.IOLoop.current().start()
