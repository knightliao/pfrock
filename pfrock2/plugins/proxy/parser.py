#!/usr/bin/env python
# coding=utf8
from pfrock2.plugins.proxy import get_proxy_handler

KEY_URL = 'url'
KEY_HOST = 'host'


class ProxyHandlerParser(object):
    @staticmethod
    def do(path, options):
        url = options[KEY_URL] if KEY_URL in options else ""
        host = options[KEY_HOST] if KEY_HOST in options else ""
        if url and path:
            return get_proxy_handler(path, url, host)
        return None
