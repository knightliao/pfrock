#!/usr/bin/env python
# coding=utf8
import os

import pfrock


def print_logo():
    logo_path = os.path.join(os.path.dirname(pfrock.__file__), "logo.txt")
    try:
        with open(logo_path, 'r') as fin:
            print fin.read()
    except:
        pass
