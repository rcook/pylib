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
import doctest
import importlib
import pkgutil

def _get_module_names(package_name):
    return ["{}.{}".format(package_name, name) for _, name, _ in pkgutil.walk_packages([package_name])]

if __name__ == "__main__":
    for name in _get_module_names("pyprelude"):
        doctest.testmod(importlib.import_module(name))
