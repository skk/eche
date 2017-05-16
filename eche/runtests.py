
import pathlib

import eche.step0_repl as step0_repl


tests_dir = pathlib.Path('eche').joinpath('tests')
tests = {
    'step0_repl.mal': step0_repl
}

for filename, mod in tests.items():
    with open(tests_dir.joinpath(filename)) as inbuf:
        lines = inbuf.read().split('\n')
        for line in lines:
            print(f"{line}")
            mod.REP(line)
