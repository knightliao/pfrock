#!/usr/bin/env python
# coding=utf8
import logging

from tornado.web import StaticFileHandler

logger = logging.getLogger('pfrock.static')


class FrockStaticDirHandler(StaticFileHandler):
    pass
