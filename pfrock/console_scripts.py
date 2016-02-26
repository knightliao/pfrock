#!/usr/bin/env python
# coding=utf8
import time

import pfrock
from pfrock.cli import argument_parser
from pfrock.cli.config_parser import PfrockConfigParser
from pfrock.cli.log import make_logging
from pfrock.cli.logo import print_logo
from pfrock.core import PFrock
from pfrock.core.handler_parser import HandlerParser

pfrockfile = 'pfrockfile.json'


def main():
    # argument parser
    debug, no_watch = argument_parser()

    # log
    make_logging(debug)
    print_logo()
    print "pfrock version %s " % pfrock.__version__
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


if __name__ == "__main__":
    main()
