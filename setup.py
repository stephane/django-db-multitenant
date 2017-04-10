#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import exists
from setuptools import setup, find_packages

README = 'README.md'

# Change package name to publish my fork on Pypi while waiting for a new upstream release
setup(
    name='webstack-django-db-multitenant',
    version='1.0',
    author=u'Stéphane Raimbault',
    author_email='stephane.raimbault@webstack.fr',
    packages=find_packages(),
    url='https://github.com/mik3y/django-db-multitenant',
    license='BSD',
    description='Multitenant support for Django, using one tenant per database.',
    long_description=open(README).read() if exists(README) else "",
    install_requires=[
        'Django >= 1.8.0',
    ],
)
