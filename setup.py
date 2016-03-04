#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import re

from pip.req import parse_requirements
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt', session=False)
# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]


def read(*names, **kwargs):
    return io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='pfrock',
    version=find_version("pfrock/__init__.py"),
    description='A plugin-based tool for running fake HTTP and socket services using Python.',
    long_description=readme,
    author='knightliao',
    author_email='knightliao@gmail.com',
    url='https://github.com/knightliao/pfrock',
    platforms='any',
    license="http://www.apache.org/licenses/LICENSE-2.0",
    packages=find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    package_data={
        'pfrock': ['logo.txt'],
        'demo': ['pfrockfile.json'],
    },
    install_requires=reqs,
    scripts=[],
    entry_points={
        'console_scripts': [
            'pfrockpy = pfrock.console_scripts:main',
        ],
    }

)
