"""
Build extension modules, package and install FrankensPy.
"""
from __future__ import absolute_import
import sys
import os
from setuptools import setup, Extension, find_packages
import numpy
import versioneer

# VERSIONEER SETUP
# #############################################################################
versioneer.VCS = 'git'
versioneer.versionfile_source = 'FrankensPy/_version.py'
versioneer.versionfile_build = 'FrankensPy/_version.py'
versioneer.tag_prefix = 'v'
versioneer.parentdir_prefix = '.'

# PACKAGE METADATA
# #############################################################################
NAME = 'frankenspy'
FULLNAME = 'FrankensPy'
DESCRIPTION = "Modeling and inversion exercises for geophysics"
AUTHOR = "Andre L. A. Reis"
AUTHOR_EMAIL = 'reisandreluis@gmail.com'
MAINTAINER = AUTHOR
MAINTAINER_EMAIL = AUTHOR_EMAIL
VERSION = versioneer.get_version()
CMDCLASS = versioneer.get_cmdclass()
LICENSE = "BSD License"
URL = "https://github.com/andrelreis/frankenspy"
PLATFORMS = "Any"
SCRIPTS = []
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Topic :: Scientific/Engineering",
    "Topic :: Software Development :: Libraries",
    "Programming Language :: Python :: 3.6",
    "License :: OSI Approved :: {}".format(LICENSE),
]
KEYWORDS = 'geophysics modeling inversion gravimetry magnetometry'

# DEPENDENCIES
# #############################################################################
INSTALL_REQUIRES = [
    'numpy',
    'scipy',
    'numba',
    'future',
    'matplotlib',
    'pillow',
    'jupyter',
    'pandas',
]
