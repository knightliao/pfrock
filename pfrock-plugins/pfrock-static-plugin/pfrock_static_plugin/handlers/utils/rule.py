# !/usr/bin/env python
# coding=utf8
import json
import logging
import re


class RuleParser(object):
    def __init__(self, rule):
        if isinstance(rule, basestring):
            self.rule = json.loads(rule)
        else:
            self.rule = rule
        self.validate(self.rule)

    class Functions(object):

        ALIAS = {
            '=': 'eq',
            '!=': 'neq',
            '>': 'gt',
            '>=': 'gte',
            '<': 'lt',
            '<=': 'lte',
            'and': 'and_',
            'in': 'in_',
            'or': 'or_',
            'not': 'not_',
            'str': 'str_',
            'int': 'int_',
            '+': 'plus',
            '-': 'minus',
            '*': 'multiply',
            '/': 'divide'
        }

        def eq(self, *args):
            return args[0] == args[1]

        def neq(self, *args):
            return args[0] != args[1]

        def in_(self, *args):
            return args[0] in args[1:]

        def gt(self, *args):
            return args[0] > args[1]

        def gte(self, *args):
            return args[0] >= args[1]

        def lt(self, *args):
            return args[0] < args[1]

        def lte(self, *args):
            return args[0] <= args[1]

        def not_(self, *args):
            return not args[0]

        def or_(self, *args):
            return any(args)

        def and_(self, *args):
            return all(args)

        def int_(self, *args):
            return int(args[0])

        def str_(self, *args):
            return unicode(args[0])

        def upper(self, *args):
            return args[0].upper()

        def lower(self, *args):
            return args[0].lower()

        def plus(self, *args):
            return sum(args)

        def minus(self, *args):
            return args[0] - args[1]

        def multiply(self, *args):
            return args[0] * args[1]

        def divide(self, *args):
            return float(args[0]) / float(args[1])

        def abs(self, *args):
            return abs(args[0])

    @staticmethod
    def validate(rule):
        if not isinstance(rule, list):
            raise Exception('Rule must be a list, got {}'.format(type(rule)))
        if len(rule) < 2:
            raise Exception('Must have at least one argument.')

    def _evaluate(self, rule, fns):
        """
        递归执行list内容
        """

        def _recurse_eval(arg):
            if isinstance(arg, list):
                return self._evaluate(arg, fns)
            else:
                return arg

        r = map(_recurse_eval, rule)
        r[0] = self.Functions.ALIAS.get(r[0]) or r[0]
        func = getattr(fns, r[0])
        # print func, r[1:]
        return func(*r[1:])

    def evaluate(self):
        fns = self.Functions()
        ret = self._evaluate(self.rule, fns)
        if not isinstance(ret, bool):
            logging.warn('In common usage, a rule must return a bool value,'
                         'but get {}, please check the rule to ensure it is true')
        return ret


class VariableRuleParser(object):
    pattern = re.compile(r'^\$\{\(?(.*)\)?\}')

    def __init__(self, rule, is_json=False, variable_map={}):
        self.variable_map = variable_map
        if is_json is True:
            self.rule = rule
        else:
            self.rule = json.loads(rule)

    def _variable_evaluate(self, rule):
        def _recurse_eval(arg):
            if isinstance(arg, list):
                return self._variable_evaluate(arg)
            else:

                match = self.pattern.match(str(arg))
                if match:
                    match_data = match.groups()[0]
                    if match_data in self.variable_map:
                        arg = self.variable_map[match_data]
                return arg

        r = map(_recurse_eval, rule)
        return r

    def evaluate_variable(self):
        # print self.rule
        ret = self._variable_evaluate(self.rule)
        # print ret
        parser = RuleParser(json.dumps(ret))
        return parser.evaluate()
