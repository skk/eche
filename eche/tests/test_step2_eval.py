
import pytest

from eche.reader import read_str
from eche.eval import eval_ast, repl_env


@pytest.mark.parametrize("test_input,expected_value", [
    ('(+ 1 2)', 3),
    ('(- 5 9)', -4),
    ('(* 50 60)', 3_000),
    ('(/ 2 2)', 1),
    ('(+ 1 (* 3 5))', 16),
    ('(^ 2 2)', 4),
    ('(^ 2 3)', 8),
    ('(% 8 5)', 3),
    ('(% (^ 2 3) 5)', 3),
    ('(+ 2 3)', 5),
    ('(+ 2 (* 3 4))', 14),
])
def test_eval_add(test_input, expected_value):
    ast = read_str(test_input)
    assert eval_ast(ast, repl_env) == expected_value
