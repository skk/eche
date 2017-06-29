import typing

from eche.printer import print_str
from eche.reader import read_str
from eche.eche_types import Node, EcheTypeBase, Env
from eche.eval import eval_ast


def print_str_and_read_str_wrapper(test_input: str, expected: typing.Any=None) -> typing.Any:
    if expected is None:
        expected = test_input

    val = read_str(test_input)
    actual = print_str(val)
    result = actual == expected
    return result


def eval_ast_and_verify_env(test_input: str, env: Env, env_key: str, env_val: Node) -> bool:
    ast = read_str(test_input)
    ast = eval_ast(ast, env)
    return ast.env[env_key] == env_val


def eval_ast_and_read_str(test_input: str, env: Env, expected_value: typing.Any) -> bool:
    ast = read_str(test_input)
    if not isinstance(expected_value, EcheTypeBase):
        expected_value = Node(data=expected_value)

    actual = eval_ast(ast, env)
    # print(f"test_input {test_input} actual {actual} ==? expected_value {expected_value}")
    return actual == expected_value
