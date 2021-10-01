#!/usr/bin/env python
# coding=utf8

import argparse
import logging

logger = logging.getLogger('pfrock.cli')


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", dest='debug',
                        help="Enable verbose (debug) logging. Default do not output debug info.")
    parser.add_argument("-w", "--nowatch ", action="store_true", dest='nowatch',
                        help="Don't watch the pfrockfile for changes. Default is watching.")
    args = parser.parse_args()
    return args.debug, args.nowatch
