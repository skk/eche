import pytest

from eche.env import get_default_env
from eche.tests import eval_ast_and_verify_env, eval_ast_and_read_str
from eche.eche_types import Node
from eche.eche_types import List
from eche.eval import eval_ast
from eche.reader import read_str
import eche.step3_env as step


@pytest.mark.parametrize("test_input,env_key,env_val", [
    ('(def! a 5)', 'a', 5),
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


@pytest.mark.parametrize("test_input,expected_value", [
    ('(let* (c 2) c)', 2),
    ('(let* (a 1 b 2) (+ a b))', 3),
    ('(let* (a 1 b 2 c 3) (+ (* a b) (^ 2 c)))', 10),
])
def test_let_star(test_input, expected_value):
    assert eval_ast_and_read_str(test_input, get_default_env(), expected_value)


@pytest.mark.parametrize("test_input,expected_output", [
    ('(print 1)', '1'),
    ('(print (* 2 2))', '4'),
])
def test_print_fn(capsys, test_input, expected_output):
    env = get_default_env()
    eval_ast(read_str(test_input), env)
    out, err = capsys.readouterr()
    assert out.strip() == expected_output
