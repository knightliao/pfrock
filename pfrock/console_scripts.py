#!/usr/bin/env python
# coding=utf8

import os
import sys
import time

import pfrock
from pfrock.cli import argument_parser
from pfrock.cli.config_parser import PfrockConfigParser
from pfrock.cli.log import make_logging
from pfrock.cli.logo import print_logo
from pfrock.core import PFrock
from pfrock.core.routes import RoutesMgr

pfrockfile = 'pfrockfile.json'


def main():
    sys.path.insert(0, os.getcwd())

    # argument parser
    debug, no_watch = argument_parser()

    # log
    make_logging(debug)
    print_logo()
    print "pfrock version %s " % pfrock.__version__
    time.sleep(1)

    # parser
    config_server = PfrockConfigParser.do(pfrockfile)

    # routes
    if config_server:
        route_list = RoutesMgr.get_routes(config_server)
        # new frock
        p_frock = PFrock(auto_reload=not no_watch, port=config_server.port)
    else:
        route_list = []
        # new frock
        p_frock = PFrock(auto_reload=not no_watch)

    p_frock.add_watch(pfrockfile)
    p_frock.add_handler(route_list)

    # start
    try:
        p_frock.start()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
