
import pathlib
import traceback

import sys

import eche.step0_repl as step0_repl
import eche.step1_read_print as step1_read_print
import eche.reader

tests_dir = pathlib.Path('eche').joinpath('tests')
tests = {
    'step0_repl.mal': step0_repl,
    'step1_read_print.mal': step1_read_print
}

for filename, mod in tests.items():
    with open(tests_dir.joinpath(filename)) as inbuf:
        lines = inbuf.read().split('\n')
        for line in lines:
            print(f"{line}")
            try:
                mod.REP(line)
            except eche.reader.Blank:
                continue
            except (SyntaxError, ValueError) as e:
                print("".join(traceback.format_exception(*sys.exc_info())))
                continue
            except IOError as e:
                print("".join(traceback.format_exception(*sys.exc_info())))
                break

