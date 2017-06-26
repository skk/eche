import traceback
import sys

from eche.eche_readline import getline
from eche.reader import read_str, Blank
from eche.printer import print_str
from eche.env import default_env
from eche.eval import eval_ast


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


def repl():  # pragma: no cover
    while True:
        try:
            line = getline(prompt_msg='user> ')
            process_line(line)
        except IOError as e:
            print("".join(traceback.format_exception(*sys.exc_info())))
            break

    return 0


def process_line(line):  # pragma: no cover
    try:
        print(line)
        print(REP(line))
    except Blank:
        return
    except (SyntaxError, ValueError, TypeError) as e:
        print("".join(traceback.format_exception(*sys.exc_info())))
        return


def process_file(input_file):  # pragma: no cover
    with open(input_file, 'r') as inbuf:
        for line in inbuf:
            process_line(line)


def main():  # pragma: no cover
    repl()

if __name__ == "__main__":  # pragma: no cover
    repl()
