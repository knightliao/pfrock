#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from pip.req import parse_requirements
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt', session=False)
# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='pfrock',
    version='0.1',
    description='A plugin-based tool for running fake HTTP and socket services using Python.',
    long_description=readme,
    author='knightliao',
    author_email='knightliao@gmail.com',
    url='http://github.com/knightliao',
    platforms='any',
    packages=find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    requires=['tornado'],
    install_requires=reqs,
    data_files=[('pfrock', ['pfrock/logo.txt'])],
    entry_points={
        'console_scripts': [
            'pfrockpy = pfrock.console_scripts:run_pfrock',
        ],
    }

)
