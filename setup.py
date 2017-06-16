# -*- coding: utf-8 -*-

from setuptools import setup


kwargs = {
    'name': 'echo',
    'version': '0.1.0',
    'description': '',
    'long_description': 'eche\n####\n\n`Build Status`_\n\nDescription\n***********\n\nA lisp-like Programming Language interpreter.  It is based on the\n`make-a-lisp`_\n\nLicense\n*******\n\nMIT License; see :download:`LICENSE.txt`_ for more details.\n\n\n.. _make-a-lisp: https://github.com/kanaka/mal\n.. _Build Status: https://travis-ci.org/skk/eche.svg?branch=master\n',
    'author': 'Steven Knight',
    'author_email': 'steven@knight.cx',
    'url': 'https://github.com/skk/echo',
    'license': 'MPL 2.0',
    'keywords': '',
    'classifiers': [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
    'entry_points': {
        'console_scripts': [
            'eche = poet:eche.main'
        ]
    },
    'install_requires': [
        'attrs>=17.2.0,<18.0.0',
        'funcy>=1.7.5,<2.0.0',
        'mypy>=0.511.0,<0.512.0',
        'pprintpp>=0.3.0,<0.4.0',
        'prompt_toolkit==1.0.5',
        'pygments==2.2.0',
        'pyreadline==2.1.0',
        'toml>=0.9.0,<0.10.0'
    ],
    'tests_require': [
        'coverage==4.4.1',
        'httpretty>=0.8.14,<0.9.0',
        'pytest>=3.0.0,<4.0.0',
        'pytest-cov>=2.4.0,<3.0.0'
    ],
    'include_package_data': True
}

setup(**kwargs)