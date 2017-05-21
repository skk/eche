# !env python

import sys
import pytest

if "-c" in sys.argv:
    sys.argv.remove("-c")
    args = ['--cov-config', '.coveragerc',
            '--cov-report', 'html',
            '--cov-report', 'term-missing',
            '--cov',
            '.']
else:
    args = []

args.append('--tb=native')
sys.argv.extend(args)

args = ' '.join(sys.argv)
print(f"sys argv {args}")

if __name__ == '__main__':
    sys.exit(pytest.main())
