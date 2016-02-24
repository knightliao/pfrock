#!/usr/bin/env python
# coding=utf8
import os

import pfrock2.bin


def print_logo():
    logo_path = os.path.join(os.path.dirname(pfrock2.bin.__file__), "logo.txt")
    try:
        with open(logo_path, 'r') as fin:
            print fin.read()
    except:
        pass
