import pytest

from eche.env import env
from eche.tests import eval_ast_and_read_str


@pytest.mark.parametrize("test_input,expected_value", [
    ('(def! a 5)', 5)
])
def test_def_exp_mark(test_input, expected_value):
    # TODO Need to test that the ENV has been updated correctly
    assert eval_ast_and_read_str(test_input, env, expected_value)
