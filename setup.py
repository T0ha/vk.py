#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
setuptools installer for VK.py
Created on Feb 1, 2012

@author: T0ha aka Shvein Anton
'''

from setuptools import setup

setup(
    name = "VK.py",
    version = "0.1",
    author = "T0ha aka Shvein Anton",
    author_email = "t0hashvein@gmail.com",
    description = ("Simple VK.API wrapper for Python 2"),
    license = "GPL v3",
    keywords = "VK vk.api",
    url = "https://github.com/T0ha/vk.py.git",
    scripts = ['vk.py'],  
    install_requires = ['grab']
)
