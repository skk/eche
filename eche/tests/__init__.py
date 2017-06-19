
from eche.printer import print_str
from eche.reader import read_str
from eche.eche_types import Node, EcheTypeBase
from eche.eval import eval_ast


def print_str_and_read_str_wrapper(test_input, expected=None):
    if expected is None:
        expected = test_input

    val = read_str(test_input)
    actual = print_str(val)
    result = actual == expected
    return result


def eval_ast_and_read_str(test_input, env, expected_value):
    ast = read_str(test_input)
    if not isinstance(expected_value, EcheTypeBase):
        expected_value = Node(data=expected_value)

    return eval_ast(ast, env) == expected_value

