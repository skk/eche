import traceback
import sys

from eche.eche_readline import getline
from eche.reader import read_str, Blank
from eche.printer import print_str
from eche.env import get_default_env
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
def REP(data, env=None):
    if env is None:
        env = get_default_env()
    return PRINT(EVAL(READ(data), env))


def repl():  # pragma: no cover
    env = get_default_env()
    result = None
    while True:
        try:
            line = getline(prompt_msg='user> ', previous_result=result)
            result = process_line(line, env)
        except IOError as e:
            print("".join(traceback.format_exception(*sys.exc_info())))
            break

    return 0


def process_line(line, env):  # pragma: no cover
    try:
        r = REP(line, env)
        if r is None:
            return
        else:
            print(r)
            return r
    except Blank:
        return
    except (SyntaxError, ValueError, TypeError) as e:
        print("".join(traceback.format_exception(*sys.exc_info())))
        return


def process_file(input_file):  # pragma: no cover
    env = get_default_env()
    with open(input_file, 'r') as inbuf:
        for line in inbuf:
            process_line(line, env)


def main():  # pragma: no cover
    repl()

if __name__ == "__main__":  # pragma: no cover
    repl()
