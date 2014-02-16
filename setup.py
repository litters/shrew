#!/usr/bin/env python

#
# Copyright 2014 the original author or authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

from io import open
import subprocess
import sys

from setuptools import find_packages, setup

from shrew import __version__


install_requires = []
tests_require = install_requires + ['coverage', 'mockito', 'nose']

setup(
    name='shrew',
    version=__version__,
    url='http://github.com/litters/shrew/',
    license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
    author='Alan D. Cabrera',
    author_email='adc@toolazydogs.com',
    description='A handy way to manage your bash environment across machines.',
    # don't ever depend on refcounting to close files anywhere else
    long_description=open('README.rst', encoding='utf-8').read(),

    packages=['shrew'],
    scripts=['bin/shrew'],
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,

    test_suite='shrew',
    tests_require=tests_require,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
