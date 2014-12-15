#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "0.1.0"

if sys.argv[-1] == 'publish':
    try:
        import wheel
    except ImportError:
        raise ImportError("Fix: pip install wheel")
    os.system('python setup.py sdist bdist_wheel upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()


readme = open('README.rst').read()

setup(
    name='ctx',
    version=version,
    description="""A minimal but opinionated dict/object combo (like Bunch).""",
    long_description=readme + '\n\n',
    author='Robert Ledger',
    author_email='figlief@figlief.com',
    url='https://github.com/figlief/ctx',
    include_package_data=True,
    py_modules=['ctx'],
    install_requires=[],
    license="BSD",
    zip_safe=False,
    keywords='ctx',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
