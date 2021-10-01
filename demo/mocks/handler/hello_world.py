#!/usr/bin/env python
# coding=utf8
from pfrock.core.web import PfrockRequestDispatcher


class HelloWorldHandler(PfrockRequestDispatcher):
    def get(self):
        self.write("Hello, world " + self.query + " " + str(self.page_no))

    def initialize(self, **kwargs):
        self.query = kwargs.get('query', "")
        self.page_no = kwargs.get('pageno', 1)
