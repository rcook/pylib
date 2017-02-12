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

def _read_readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="pyprelude",
    version="0.1",
    description="General-purpose Python support functions",
    long_description=_read_readme(),
    url="https://github.com/rcook/pyprelude",
    author="Richard Cook",
    author_email="rcook@rcook.org",
    license="MIT",
    packages=["pyprelude"],
    include_package_data=True,
    zip_safe=False)
