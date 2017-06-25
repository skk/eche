import pytest

from eche.env import default_env
from eche.tests import eval_ast_and_verify_env
from eche.eche_types import Node


@pytest.mark.parametrize("test_input,env_key,env_val", [
    ('(def! a 5)', 'a', 5),
    ('(def! b (- 10 0))', 'b', 10)
])
def test_def_exp_mark(test_input, env_key, env_val):
    assert eval_ast_and_verify_env(test_input, default_env, env_key, Node(data=env_val))
