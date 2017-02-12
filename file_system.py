############################################################
#
# pylib.file_system
# Copyright (C) 2017, Richard Cook
# Release under MIT License
# https://github.com/rcook/pylib
#
############################################################

from __future__ import print_function
import stat

def _on_error(func, path, exc_info):
    if os.access(path, os.W_OK):
        raise
    else:
        os.chmod(path, stat.S_IWUSR)
        func(path)

def remove_dir(dir):
    # TODO: Consider using robocopy on Windows
    shutil.rmtree(dir, onerror=_on_error)
