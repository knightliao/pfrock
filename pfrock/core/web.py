#!/usr/bin/env python
# coding=utf8
import tornado
from tornado.web import RedirectHandler, _unquote_or_none, ErrorHandler

from pfrock.core.constants import ROUTER_METHOD


class MyApplication(tornado.web.Application):
    def start_request(self, server_conn, request_conn):
        # Modern HTTPServer interface
        return _MyRequestDispatcher(self, request_conn)

    def __call__(self, request):
        # Legacy HTTPServer interface
        dispatcher = _MyRequestDispatcher(self, None)
        dispatcher.set_request(request)
        return dispatcher.execute()


class _MyRequestDispatcher(tornado.web._RequestDispatcher):
    def _find_handler(self):
        # Identify the handler to use as soon as we have the request.
        # Save url path arguments for later.
        app = self.application
        handlers = app._get_host_handlers(self.request)
        if not handlers:
            self.handler_class = RedirectHandler
            self.handler_kwargs = dict(url="%s://%s/" % (self.request.protocol, app.default_host))
            return
        for spec in handlers:
            match = spec.regex.match(self.request.path)
            if match:

                has_method_defined = ROUTER_METHOD in spec.kwargs
                if (not has_method_defined) or spec.kwargs.get(ROUTER_METHOD,
                                                               []) == [] or self.request.method.upper() in spec.kwargs.get(
                    ROUTER_METHOD, []):

                    self.handler_class = spec.handler_class
                    self.handler_kwargs = spec.kwargs
                    if spec.regex.groups:
                        # Pass matched groups to the handler.  Since
                        # match.groups() includes both named and
                        # unnamed groups, we want to use either groups
                        # or groupdict but not both.
                        if spec.regex.groupindex:
                            self.path_kwargs = dict(
                                (str(k), _unquote_or_none(v))
                                for (k, v) in match.groupdict().items())
                        else:
                            self.path_args = [_unquote_or_none(s)
                                              for s in match.groups()]
                    return

        if app.settings.get('default_handler_class'):
            self.handler_class = app.settings['default_handler_class']
            self.handler_kwargs = app.settings.get(
                'default_handler_args', {})
        else:
            self.handler_class = ErrorHandler
            self.handler_kwargs = dict(status_code=404)


class PfrockRequestDispatcher(tornado.web.RequestHandler):
    def initialize(self, **kwargs):
        pass
