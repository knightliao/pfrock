#!/usr/bin/env python
# coding=utf8
from pfrock.core import logger
from pfrock.core.plugin import PfrockPlugin


class PfrockPluginRegister(object):
    register_class_plugins = {}

    @classmethod
    def register(cls, handler_class):
        r_index = handler_class.__module__.rfind('.')
        module = handler_class.__module__[0:r_index]

        bases = handler_class.__bases__
        for base in bases:
            if base == PfrockPlugin:

                invert_op = getattr(handler_class, PfrockPlugin.get_handler.__name__, None)
                if callable(invert_op):
                    cls.register_class_plugins[module] = handler_class
                    # logger.debug("register plugin %s " % handler_class)
                    return
                else:
                    logger.warn("cannot find parser_to_handlers in %s " % handler_class)

        logger.warn("cannot register plugin %s " % handler_class)

    @classmethod
    def get_handler(cls, module_name):
        return cls.register_class_plugins[module_name] if module_name in cls.register_class_plugins else None
