#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yong'

from cx_Freeze import setup,Executable

includefiles = [ 'README.md','down.ico']
includes = ['requests']
excludes = ['Tkinter']
packages = ['sys',]

setup(
    name = 'down',
    version = '1.0',
    description = 'A downloader.',
    author = 'yong',
    author_email = '12374011@163.com',
    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
    executables = [Executable('cat.py',icon = "down.ico")]
)