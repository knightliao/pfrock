#!/usr/bin/env python
# coding=utf8

import importlib
import logging

logger = logging.getLogger('pfrock.handler')


def import_from_file(class_path):
    r_index = class_path.rfind('.')
    module = importlib.import_module(class_path[0:r_index])
    my_class = getattr(module, class_path[r_index + 1:])
    return my_class


def add_handler(p_frock, url, handler_path):
    my_class = import_from_file(handler_path)
    handler = (url, my_class)
    p_frock.add_handler([handler])
