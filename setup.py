#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: thepoy
# @Email: thepoy@163.com
# @File Name: setup.py (c) 2021
# @Created:  2021-05-27 08:37:45
# @Modified: 2021-05-27 08:58:26

import codecs
import colort

from setuptools import setup

with codecs.open("README.md", "r", "utf-8") as fd:
    setup(
        name="colort",
        version=colort.__version__,
        description='''
        Display colored text in the terminal
        ''',
        long_description_content_type="text/markdown",
        long_description=fd.read(),
        author="thepoy",
        author_email="thepoy@163.com",
        url="https://github.com/thep0y/colort",
        license="MIT",
        keywords="color terminal",
    )
