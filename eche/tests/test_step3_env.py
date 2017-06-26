import pytest

from eche.env import get_default_env
from eche.tests import eval_ast_and_verify_env
from eche.eche_types import Node
from eche.eche_types import List
import eche.step3_env as step


@pytest.mark.parametrize("test_input,env_key,env_val", [
    # ('(def! a 5)', 'a', 5),
    ('(def! b (- 10 0))', 'b', 10)
])
def test_def_exp_mark(test_input, env_key, env_val):
    assert eval_ast_and_verify_env(test_input, get_default_env(), env_key, Node(data=env_val))


@pytest.mark.parametrize("test_input", [
    '(7 8)'
])
def test_read(test_input):
    assert step.READ(test_input) == List(7, 8)


@pytest.mark.parametrize("test_input", [
    '(1 2 3)',
    '(+ 1 2)'
])
def test_eval(test_input):
    assert step.EVAL(test_input, None) == test_input


@pytest.mark.parametrize("test_input", [
    '(- 2 3)',
    '(% 1 2)'
])
def test_print(test_input):
    assert step.PRINT(test_input) == test_input


@pytest.mark.parametrize("test_input", [
    '(+ 2 3)',
    '[5 6 7]'
])
def test_rep(test_input):
    assert step.REP(test_input)