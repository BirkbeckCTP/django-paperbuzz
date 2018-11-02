#!/usr/bin/env python

from distutils.core import setup


def readme():
    with open('README.md') as f:
        return f.read()


kwargs = {
    'name': 'paperbuzz',
    'version': '0.1',
    'description': "A django application for Paperbuzz metrics.",
    'keywords': 'Open Library of Humanities Paperbuzz PKP',
    'author': 'Andy Byers',
    'author_email': 'tech@openlibhums.org',
    'url': 'https://github.com/birkbeckctp/django-paperbuzz',
    'license': 'MIT',
    'packages': ['paperbuzz'],
    'zip_safe': False,
    'install_requires': [],
}

setup(**kwargs)