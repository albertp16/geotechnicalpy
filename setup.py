# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 18:24:47 2022

@author: albertp16
"""
from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Geotechnical Engineering Python library'
LONG_DESCRIPTION = ''

# Setting up..
setup(
    name="geotechnicalpy",
    version=VERSION,
    author="albertp16 (Albert Pamonag)",
    author_email="<albertpamonag@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
