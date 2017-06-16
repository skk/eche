
import pytest

from eche.reader import read_str
from eche.eval import eval_ast, repl_env
from eche_types import Node


@pytest.mark.parametrize("test_input,expected_value", [
    ('(+ 1 2)', 3),
    ('(+ 2 3)', 5),
    ('(+ 2 (* 3 4))', 14),
])
def test_eval_add(test_input, expected_value):
    ast = read_str(test_input)
    assert eval_ast(ast, repl_env) == Node(data=expected_value)


@pytest.mark.parametrize("test_input,expected_value", [
    ('(- 5 9)', -4),
     ('(- 1 0)', 1),
])
def test_eval_sub(test_input, expected_value):
    ast = read_str(test_input)
    assert eval_ast(ast, repl_env) == Node(data=expected_value)


@pytest.mark.parametrize("test_input,expected_value", [
    ('(* 50 60)', 3_000),
    ('(* 2 3)', 6),
    ('(+ 2 (* 3 4))', 14),
])
def test_eval_mul(test_input, expected_value):
    ast = read_str(test_input)
    assert eval_ast(ast, repl_env) == Node(data=expected_value)


@pytest.mark.parametrize("test_input,expected_value", [
    ('(/ 2 2)', 1),
])
def test_eval_div(test_input, expected_value):
    ast = read_str(test_input)
    assert eval_ast(ast, repl_env) == Node(data=expected_value)


@pytest.mark.parametrize("test_input,expected_value", [
    ('(^ 2 2)', 8),
    ('(^ 3 4)', 81),
    ('(^ 10^10)', 10_000_000_000),
])
def test_eval_exp(test_input, expected_value):
    ast = read_str(test_input)
    assert eval_ast(ast, repl_env) == Node(data=expected_value)


@pytest.mark.parametrize("test_input,expected_value", [
    ('(% 8 5)', 3),
    ('(% (^ 2 3) 5)', 3),
])
def test_eval_exp(test_input, expected_value):
    ast = read_str(test_input)
    assert eval_ast(ast, repl_env) == Node(data=expected_value)
