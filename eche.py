#!env python

"""Eche - a simple, lisp like language.

Usage:
    eche FILE ...
    eche (-h | --help)
    eche --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""


import sys
import pathlib

from docopt import docopt

sys.path.append(str(pathlib.Path('.').joinpath('eche')))
import eche.step3_env as eche

VERSION = '0.3.1'


def main():
    args = docopt(__doc__, version=VERSION)
    if args['--version']:
        print(VERSION)
        sys.exit(0)

    if 'FILE' in args:
        for filename in args['FILE']:
            eche.process_file(filename)
    else:
        sys.exit(eche.repl())

if __name__ == "__main__":
    main()
