#!/usr/bin/env python
############################################################
#
# pyprelude
# Copyright (C) 2017, Richard Cook
# Release under MIT License
# https://github.com/rcook/pyprelude
#
############################################################

from __future__ import print_function
from setuptools import setup

setup(
    name="pyprelude",
    version="0.1",
    description="General-purpose Python support functions",
    setup_requires=["setuptools-markdown"],
    long_description_markdown_filename="README.md",
    url="https://github.com/rcook/pyprelude",
    author="Richard Cook",
    author_email="rcook@rcook.org",
    license="MIT",
    packages=["pyprelude"],
    include_package_data=True,
    test_suite="pyprelude.tests.suite",
    zip_safe=False)
