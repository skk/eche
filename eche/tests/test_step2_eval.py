import pytest

from eche.env import env
from eche.eche_types import List
from eche.tests import eval_ast_and_read_str
import eche.step2_eval as step


@pytest.mark.parametrize("test_input,expected_value", [
    ('(+ 1 2)', 3),
    ('(+ 2 3)', 5),
    ('(+ 2 (* 3 4))', 14),
])
def test_eval_add(test_input, expected_value):
    assert eval_ast_and_read_str(test_input, env, expected_value)


@pytest.mark.parametrize("test_input,expected_value", [
    ('(- 5 9)', -4),
    ('(- 1 0)', 1),
])
def test_eval_sub(test_input, expected_value):
    assert eval_ast_and_read_str(test_input, env, expected_value)


@pytest.mark.parametrize("test_input,expected_value", [
    ('(* 50 60)', 3_000),
    ('(* 2 3)', 6),
    ('(+ 2 (* 3 4))', 14),
])
def test_eval_mul(test_input, expected_value):
    assert eval_ast_and_read_str(test_input, env, expected_value)


@pytest.mark.parametrize("test_input,expected_value", [
    ('(/ 2 2)', 1),
])
def test_eval_div(test_input, expected_value):
    assert eval_ast_and_read_str(test_input, env, expected_value)


@pytest.mark.parametrize("test_input,expected_value", [
    ('(^ 2 2)', 8),
    ('(^ 3 4)', 81),
    ('(^ 10^10)', 10_000_000_000),
])
def test_eval_exp(test_input, expected_value):
    assert eval_ast_and_read_str(test_input, env, expected_value)


@pytest.mark.parametrize("test_input,expected_value", [
    ('(% 8 5)', 3),
    ('(% (^ 2 3) 5)', 3),
])
def test_eval_exp(test_input, expected_value):
    assert eval_ast_and_read_str(test_input, env, expected_value)


@pytest.mark.parametrize("test_input,expected_value", [
    ('[1, 2, 3]', [1, 2, 3]),
])
def test_eval_vector(test_input, expected_value):
    assert eval_ast_and_read_str(test_input, env, expected_value)


@pytest.mark.parametrize("test_input", [
    '(7 8)'
])
def test_read(test_input):
    assert step.READ(test_input) == List(7, 8)


@pytest.mark.parametrize("test_input", [
    '(1 2 3)',
    '(+ 1 3)'
])
def test_eval(test_input):
    assert step.EVAL(test_input, None) == test_input


@pytest.mark.parametrize("test_input", [
    '(- 2 3)',
    '(% 1 6)'
])
def test_print(test_input):
    assert step.PRINT(test_input) == test_input


@pytest.mark.parametrize("test_input", [
    '(+ 2 3)',
    '[5 6 7]'
])
def test_rep(test_input):
    assert step.REP(test_input)
