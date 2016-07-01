#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yong'
import requests
from cx_Freeze import setup,Executable

includefiles = [ 'README.md','down.ico',(requests.certs.where(), 'cacert.pem'),'LICENSE.txt']
includes = ['requests']
excludes = ['Tkinter']
packages = ['sys',]

setup(
    name = 'down',
    version = '1.0',
    description = 'A downloader.',
    author = 'yong',
    author_email = '12374011@163.com',
    requires = ["requests"],
    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
    executables = [Executable('mycat.py',icon = "down.ico")]
)