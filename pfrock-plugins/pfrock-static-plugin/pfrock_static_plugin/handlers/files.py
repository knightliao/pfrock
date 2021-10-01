#!/usr/bin/env python
# coding=utf8
from tornado.web import os

from pfrock_static_plugin.handlers import ROUTER_HEADER, ROUTER_STATIC_FILES, ROUTER_STATIC_FILE
from pfrock_static_plugin.handlers.file import FrockStaticFileHandler
from pfrock_static_plugin.handlers.utils.rule import VariableRuleParser

ROUTER_STATIC_FILE_RULE = 'rule'


class FrockStaticFilesHandler(FrockStaticFileHandler):
    def post(self):
        return self.get()

    def delete(self):
        return self.get()

    def put(self):
        return self.get()

    def initialize(self, **kwargs):

        # get argument map
        argument_map = {}
        for argu in self.request.arguments:
            argument_map[argu] = self.request.arguments[argu][-1]

        #
        has_found_rule = False
        target_file_path = None

        # search match rule
        cur_rule_files = kwargs.get(ROUTER_STATIC_FILES, [])
        for rule_file in cur_rule_files:
            rule = rule_file[ROUTER_STATIC_FILE_RULE]
            try:

                # no rule should pass
                if rule is "":
                    is_valid = True
                else:
                    variable_rule_parser = VariableRuleParser(rule, True, argument_map)
                    is_valid = variable_rule_parser.evaluate_variable()

                if is_valid is True:
                    has_found_rule = True
                    target_file_path = rule_file[ROUTER_STATIC_FILE]
                    break
            except Exception, e:
                # when no found , return 404 just ok
                self.set_status(404)

        # match should return or return 404
        if has_found_rule:
            super(FrockStaticFilesHandler, self).initialize(target_file_path, **kwargs)
        else:
            self.set_status(404)

    @staticmethod
    def get_handler(url, options):

        # rule files
        valid_rule_files = []
        rule_files = options[ROUTER_STATIC_FILES] if ROUTER_STATIC_FILES in options else []
        for rule_file in rule_files:
            if ROUTER_STATIC_FILE_RULE not in rule_file:
                rule_file[ROUTER_STATIC_FILE_RULE] = ""
            if ROUTER_STATIC_FILE in rule_file:
                if os.path.exists(rule_file[ROUTER_STATIC_FILE]):
                    valid_rule_files.append(rule_file)

        # header
        headers = options[ROUTER_HEADER] if ROUTER_HEADER in options else {}

        if len(valid_rule_files) != 0:
            handler = (url, FrockStaticFilesHandler, {ROUTER_STATIC_FILES: valid_rule_files, ROUTER_HEADER: headers})
        else:
            handler = None

        return handler
