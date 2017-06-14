import traceback
import sys

import pprintpp

from eche.eche_readline import getline
from eche.reader import read_str, Blank
from eche.printer import print_str


# noinspection PyPep8Naming
def READ(data):
    return read_str(data)


# noinspection PyPep8Naming
def EVAL(ast, _):
    pprintpp.pprint(ast)
    return ast


# noinspection PyPep8Naming
def PRINT(exp):
    return print_str(exp)


# noinspection PyPep8Naming
def REP(data):
    return PRINT(EVAL(READ(data), {}))


def repl():
    while True:
        try:
            line = getline(prompt_msg='user> ')
            if line is None:
                break
            if line == '':
                continue
            print(REP(line))
        except Blank:
            continue
        except SyntaxError as e:
            print("".join(traceback.format_exception(*sys.exc_info())))
            continue
        except IOError as e:
            print("".join(traceback.format_exception(*sys.exc_info())))
            break

    return 0


def main():
    repl()


if __name__ == "__main__":
    main()
