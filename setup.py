#!/usr/bin/env python

import os
import sys

#import PPL_Assignment

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = ['Source']

requires = []

with open('README.rst') as f:
    readme = f.read()

setup(
    name='PPL_Assignment',
    version='1.0',
    description='Server Data Analyser',
    long_description=readme,
    author='Nirlendu Saha',
    author_email='nirlendu@gmail.com',
    url='',
    packages=packages,
    package_data={},
    package_dir={},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Pocket Play Labs',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',

    ),
)
