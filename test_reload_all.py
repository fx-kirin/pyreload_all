#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 zenbook <zenbook@zenbook-XPS>
#

import unittest
import reload_all
import os
import time

class Test(unittest.TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        with open("foo_python_module.py", "w") as f:
            f.write("print(\"first import\")")
        import foo_python_module
        reload_all.reload_all()
        time.sleep(1)
        with open("foo_python_module.py", "w") as f:
            f.write("print(\"reloaded\")")
        reload_all.reload_all()

if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
