#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 fx-kirin
#
# Distributed under terms of the MIT license.

"""

"""

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension
setup(
    name='reload_all',
    version='0.05',
    description='Reload all modified modules for 2.7 and 3.x',
    long_description='',
    author='fx-kirin',
    author_email='ono.kirin@gmail.com',
    url='https://github.com/fx-kirin/pyreload_all',
    download_url='',
    packages=['']
)
