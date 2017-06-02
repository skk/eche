#!env python

import subprocess
import sys

args = 'mypy --ignore-missing-imports .'.split(' ')
sys.exit(subprocess.call(args))
