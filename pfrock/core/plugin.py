#!/usr/bin/env python
# coding=utf8


class PfrockPlugin(object):
    def get_handler(self, options, **kwargs):
        raise NotImplementedError()
