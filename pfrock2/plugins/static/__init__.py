#!/usr/bin/env python
# coding=utf8
from pfrock2.core.constants import ROUTER_STATIC_DIR, ROUTER_STATIC_FILE, ROUTER_PATH
from pfrock2.plugins.static.dir import FrockStaticDirHandler
from pfrock2.plugins.static.file import FrockStaticFileHandler

SUPPORT_TYPE = [ROUTER_STATIC_DIR, ROUTER_STATIC_FILE]


def get_static_resolve_handler(cur_type):
    if cur_type in SUPPORT_TYPE:

        if cur_type == ROUTER_STATIC_DIR:
            return FrockStaticDirHandler
        elif cur_type == ROUTER_STATIC_FILE:
            return FrockStaticFileHandler
    return None


def add_static_handler(p_frock, cur_type, url, path):
    resolve_handler = get_static_resolve_handler(cur_type)
    if resolve_handler:
        handler = (url, resolve_handler, {ROUTER_PATH: path})
        p_frock.add_handler([handler])