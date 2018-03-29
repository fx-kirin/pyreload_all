#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 zenbook <zenbook@zenbook-XPS>
#

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
import reload_all
import time
from shutil import copyfile

class Test(unittest.TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        copyfile("foo_python_module_1.py", "foo_python_module.py")
        import foo_python_module
        foo_python_module.mymethod()
        myclass = foo_python_module.MyClass()
        myclass.my_instance_method()
        time.sleep(1)
        copyfile("foo_python_module_2.py", "foo_python_module.py")
        reload_all.reload_all(locals())
        foo_python_module.mymethod()
        myclass.my_instance_method()

if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
