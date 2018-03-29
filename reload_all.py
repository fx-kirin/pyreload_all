#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 zenbook <zenbook@zenbook-XPS>
#
# Distributed under terms of the MIT license.

"""

"""

from __future__ import print_function
import sys
import os
import re

if sys.version_info[0] == 3:
    from importlib import reload
    
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SYS_PREFIX = os.path.dirname(os.path.dirname(sys.executable))+'/lib'

def reload_all():
    for k, v in sys.modules.items():
        if not hasattr(v, '__file__'):
            continue
        elif v.__file__.startswith(SYS_PREFIX):
            continue
        elif k == '__main__':
            continue
        elif v.__file__ == __file__:
            continue
        elif re.match(".+\.pyc$", v.__file__):
            py_file_path = v.__file__[:-1]
            if os.path.exists(py_file_path):
                if os.path.getmtime(py_file_path) > os.path.getmtime(v.__file__):
                    os.remove(v.__file__)
        reload(v)
