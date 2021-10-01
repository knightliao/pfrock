#!/usr/bin/env python
# coding=utf8
import logging

from pfrock.core.plugin import PLUGIN_CLASS_KEY_REGISTER, PLUGIN_CLASS_GET_HANDLER

logger = logging.getLogger('pfrock.register')


class PfrockPluginRegister(object):
    register_class_plugins = {}

    @classmethod
    def register(cls, module_class, module_name):

        if hasattr(module_class, PLUGIN_CLASS_KEY_REGISTER):

            handler_class = getattr(module_class, PLUGIN_CLASS_KEY_REGISTER)
            invert_op = getattr(handler_class, PLUGIN_CLASS_GET_HANDLER, None)
            if callable(invert_op):
                cls.register_class_plugins[module_name] = handler_class
                # logger.debug("register plugin %s " % handler_class)
                return
            else:
                logger.warn("cannot find %s in %s " % (PLUGIN_CLASS_GET_HANDLER, handler_class))
                return

        logger.warn("cannot find %s in %s " % (PLUGIN_CLASS_KEY_REGISTER, module_class))

    @classmethod
    def get_handler(cls, module_name):
        return cls.register_class_plugins[module_name] if module_name in cls.register_class_plugins else None
