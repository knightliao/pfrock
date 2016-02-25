#!/usr/bin/env python
# coding=utf8

import logging

import tornado.httpclient
import tornado.httpserver
import tornado.httputil
import tornado.ioloop
import tornado.iostream
import tornado.options
import tornado.web

from pfrock.core.constants import ROUTER_METHOD, ROUTER_PROXY_URL

logger = logging.getLogger('pfrock.proxy')


def fetch_request(url, callback, **kwargs):
    req = tornado.httpclient.HTTPRequest(url, **kwargs)
    client = tornado.httpclient.AsyncHTTPClient()
    client.fetch(req, callback, raise_error=False)


class ProxyHandler(tornado.web.RequestHandler):
    SUPPORTED_METHODS = ['GET', 'POST', 'PUT', 'DELETE']

    def initialize(self, proxy_url="", header_host="", **kwargs):
        self.proxy_url = proxy_url
        self.header_host = header_host

    def compute_etag(self):
        return None  # disable tornado Etag

    @tornado.web.asynchronous
    def get(self):

        request_url = "%s%s" % (self.proxy_url, self.request.uri)

        logger.debug('Handle %s request to %s', self.request.method,
                     request_url)

        def handle_response(response):
            if (response.error and not
            isinstance(response.error, tornado.httpclient.HTTPError)):
                self.set_status(500)
                self.write('Internal server error:\n' + str(response.error))
            else:
                self.set_status(response.code, response.reason)
                self._headers = tornado.httputil.HTTPHeaders()  # clear tornado default header

                for header, v in response.headers.get_all():
                    if header not in ('Content-Length', 'Transfer-Encoding', 'Content-Encoding', 'Connection'):
                        self.add_header(header, v)  # some header appear multiple times, eg 'Set-Cookie'

                if response.body:
                    self.set_header('Content-Length', len(response.body))
                    self.write(response.body)
            self.finish()

        body = self.request.body
        if not body:
            body = None
        try:
            if 'Proxy-Connection' in self.request.headers:
                del self.request.headers['Proxy-Connection']
            if self.header_host:
                self.request.headers["Host"] = self.header_host
            fetch_request(
                request_url, handle_response,
                method=self.request.method, body=body,
                headers=self.request.headers, follow_redirects=False,
                allow_nonstandard_methods=True)
        except tornado.httpclient.HTTPError as e:
            if hasattr(e, 'response') and e.response:
                handle_response(e.response)
            else:
                self.set_status(500)
                self.write('Internal server error:\n' + str(e))
                self.finish()

    @tornado.web.asynchronous
    def post(self):
        return self.get()

    @tornado.web.asynchronous
    def put(self):
        return self.get()

    @tornado.web.asynchronous
    def delete(self):
        return self.get()


def add_proxy_handler(p_frock, url, methods, proxy_url, header_host=""):
    p_frock.add_handler([get_proxy_handler(url, methods, proxy_url, header_host)])


def get_proxy_handler(url, methods, proxy_url, header_host=""):
    handler = (url, ProxyHandler, {ROUTER_METHOD: methods, ROUTER_PROXY_URL: proxy_url, "header_host": header_host})
    return handler
