#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vol
from setuptools import setup, find_packages

install_requires = [
    'docopt',
]

entry_points = {
    'console_scripts': [
        'vol = vol.main:main',
    ]
}

packages = find_packages()

setup(
    name='vol',
    version=vol.__version__,
    author='Bernhard Maeser',
    author_email='bernhard.maeser@gmail.com',
    url='https://github.com/bmaeser/vol',
    license="MIT",
    description="pythonic devops toolbelt",
    long_description=open('README.rst').read(),
    packages = packages,
    include_package_data=True,
    install_requires = install_requires,
    zip_safe=False,
    entry_points=entry_points,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Operating System :: MacOS :: MacOS X',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Utilities',
    ),
)