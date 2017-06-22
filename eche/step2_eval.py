import traceback
import sys

from eche.eche_readline import getline
from eche.reader import read_str, Blank
from eche.printer import print_str

from eche.eval import eval_ast
from eche.env import default_env


# noinspection PyPep8Naming
def READ(data):
    return read_str(data)


# noinspection PyPep8Naming
def EVAL(ast, env):
    return eval_ast(ast, env)


# noinspection PyPep8Naming
def PRINT(exp):
    return print_str(exp)


# noinspection PyPep8Naming
def REP(data):
    return PRINT(EVAL(READ(data), default_env))


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
