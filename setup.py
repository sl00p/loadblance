#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
from loadblance import __version__

setup(
    name="loadblance",
    version=__version__,
    url="",
    license="MIT",
    description="Web loadblance for proxy",
    long_description=open("README.md").read(),
    author="sl00p",
    author_email="",
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
    ],
)
