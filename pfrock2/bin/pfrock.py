#!/usr/bin/env python
# coding=utf8
import time

from pfrock2.cli import argument_parser
from pfrock2.cli.config_parser import PfrockConfigParser
from pfrock2.cli.log import make_logging
from pfrock2.cli.logo import print_logo
from pfrock2.core import PFrock
from pfrock2.core.handler_parser import HandlerParser

pfrockfile = 'pfrockfile.json'


def run_pfrock():
    # argument parser
    debug, no_watch = argument_parser()

    # log
    make_logging(debug)
    print_logo()
    time.sleep(1)

    # parser
    config_server = PfrockConfigParser.do(pfrockfile)
    handlers = HandlerParser.get_handlers(config_server)

    #
    p_frock = PFrock(auto_reload=not no_watch, port=config_server.port)
    p_frock.add_watch(pfrockfile)
    p_frock.add_handler(handlers)

    # start
    try:
        p_frock.start()
    except KeyboardInterrupt:
        pass
