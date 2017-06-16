
import pytest

from eche.reader import read_str
from eche.eval import eval_ast, repl_env


@pytest.mark.parametrize("test_input,expected_value", [
    ('(+ 1 2)', 3),
    ('(+ 2 3)', 5),
    ('(+ 2 (* 3 4))', 14),
])
def test_eval_add(test_input, expected_value):
    ast = read_str(test_input)
    assert eval_ast(ast, repl_env) == expected_value


@pytest.mark.parametrize("test_input,expected_value", [
    ('(- 5 9)', -4),
     ('(- 1 0)', 1),
])
def test_eval_sub(test_input, expected_value):
    ast = read_str(test_input)
    assert eval_ast(ast, repl_env) == expected_value


@pytest.mark.parametrize("test_input,expected_value", [
    ('(* 50 60)', 3_000),
    ('(* 2 3)', 8),
    ('(+ 2 (* 3 4))', 14),
])
def test_eval_mul(test_input, expected_value):
    ast = read_str(test_input)
    assert eval_ast(ast, repl_env) == expected_value


@pytest.mark.parametrize("test_input,expected_value", [
    ('(/ 2 2)', 1),
])
def test_eval_div(test_input, expected_value):
    ast = read_str(test_input)
    assert eval_ast(ast, repl_env) == expected_value


@pytest.mark.parametrize("test_input,expected_value", [
    ('(^ 1 2)', 0.5),
    ('(^ 3 4)', 0.75),
    ('(^ 3 4)', 0.75),
])
def test_eval_exp(test_input, expected_value):
    ast = read_str(test_input)
    assert eval_ast(ast, repl_env) == expected_value

@pytest.mark.parametrize("test_input,expected_value", [
    ('(% 8 5)', 3),
    ('(% (^ 2 3) 5)', 3),
])
def test_eval_exp(test_input, expected_value):
    ast = read_str(test_input)
    assert eval_ast(ast, repl_env) == expected_value
