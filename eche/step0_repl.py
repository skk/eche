import traceback
import sys

from eche.eche_readline import getline


# noinspection PyPep8Naming
def READ(data):
    return data


# noinspection PyPep8Naming,PyUnusedLocal
def EVAL(ast, env):
    return ast


# noinspection PyPep8Naming
def PRINT(exp):
    return exp


# noinspection PyPep8Naming
def REP(data):
    return PRINT(EVAL(READ(data), {}))


def repl():  # pragma: no cover
    while True:
        try:
            line = getline(prompt_msg='user> ')
            if line is None:
                break
            if line == '':
                continue
            print(REP(line))
        except IOError as e:
            print("".join(traceback.format_exception(*sys.exc_info())))
            break

    return 0


def main():  # pragma: no cover
    repl()

if __name__ == "__main__":  # pragma: no cover
    main()