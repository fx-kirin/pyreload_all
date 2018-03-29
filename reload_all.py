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
import inspect

if sys.version_info[0] == 3:
    from importlib import reload
    from importlib.util import cache_from_source
    
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SYS_PREFIX = os.path.dirname(os.path.dirname(sys.executable))+'/lib'

def reload_all(locals_=None):
    for k, v in sys.modules.items():
        if not hasattr(v, '__file__'):
            continue
        elif v.__file__.startswith(SYS_PREFIX):
            continue
        elif k == '__main__':
            continue
        elif v.__file__ == __file__:
            continue
        if sys.version_info[0] == 2:
            if re.match(".+\.pyc$", v.__file__):
                py_file_path = v.__file__[:-1]
                if os.path.exists(py_file_path):
                    if os.path.getmtime(py_file_path) > os.path.getmtime(v.__file__):
                        print("reload %s"%(v.__file__))
                        reload(v)
                        reload_class_if_exist(v, locals_)
            elif re.match(".+\.py$", v.__file__):
                pyc_file_path = v.__file__ + "c"
                if os.path.exists(pyc_file_path):
                    if os.path.getmtime(v.__file__) > os.path.getmtime(pyc_file_path):
                        print("reload %s"%(v.__file__))
                        reload(v)
                        reload_class_if_exist(v, locals_)
        elif sys.version_info[0] == 3:
            if re.match(".+\.py$", v.__file__):
                pyc_file_path = cache_from_source(v.__file__)
                if os.path.exists(pyc_file_path):
                    if os.path.getmtime(v.__file__) > os.path.getmtime(pyc_file_path):
                        print("reload %s"%(v.__file__))
                        reload(v)
                        reload_class_if_exist(v, locals_)
                        

def reload_class_if_exist(v, variables):
    for key, value in variables.iteritems():
        if hasattr(value, '__class__'):
            if hasattr(value, '__dict__'):
                reload_class_if_exist(v, value.__dict__)
            if hasattr(value, '__module__'):
                if value.__class__.__module__ == v.__name__:
                    if hash(value.__class__) != hash(getattr(v, value.__class__.__name__)):
                        value.__class__ = getattr(v, value.__class__.__name__)
                        print("Reload class %s %s"%(key, value))
