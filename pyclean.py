#!/usr/bin/env python

# The MIT License (MIT)
#
# Copyright (c) 2015 Bartosz Zaczynski
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
ST3 plugin for removal of Python binary artifacts such as *.pyc files.

Put this in:
~/.config/sublime-text-3/Packages/PyClean/pyclean.py
"""

import os
import os.path
import shutil

import sublime
import sublime_plugin


class PyCleanCommand(sublime_plugin.WindowCommand):
    """Command used by this plugin.

    To test in ST3 console:
    window.run_command('py_clean')
    """

    def run(self):
        """Command entry point."""
        total_removed = [0, 0]
        for parent in self.window.folders():
            num_removed = remove(get_paths_to_remove(parent))
            total_removed = [sum(x) for x in zip(total_removed, num_removed)]

        if sum(total_removed) > 0:
            sublime.message_dialog(
                'Deleted {0} files and {1} folders.'.format(*total_removed))


def check_dir(name):
    """Return true when the folder can be safely removed."""
    return name in ('build', 'dist') or name.endswith('.egg-info')


def check_file(name):
    """Return true when the file can be safely removed."""
    return name.endswith('.pyc') or name.endswith('.pyo')


def get_paths_to_remove(parent_path):
    """Return a list of absolute paths to files and folders to be removed."""

    paths = []
    for root, dirs, files in os.walk(parent_path):

        for dir_name in dirs:
            if check_dir(dir_name):
                paths.append(os.path.join(root, dir_name))

        for file_name in files:
            if check_file(file_name):
                paths.append(os.path.join(root, file_name))

    return sorted(paths)


def remove(paths):
    """Recursively remove files and folders, return list with counts."""
    num_removed = [0, 0]
    for path in paths:
        if os.path.isdir(path):
            print('Removing directory {0}'.format(path))
            shutil.rmtree(path)
            num_removed[1] += 1
        else:
            print('Removing file {0}'.format(path))
            os.remove(path)
            num_removed[0] += 1
    return num_removed
