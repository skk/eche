import pytest

from eche.eche_types import EcheTypeBase, Keyword, Env, Symbol


def test_eche_type_base():
    b = EcheTypeBase(None)
    assert isinstance(b, EcheTypeBase) and b.value is None

    b = EcheTypeBase(1)
    assert isinstance(b, EcheTypeBase) and b.value == 1


def test_keyword():
    value = 'if'
    kw = Keyword(value)
    assert kw.value == value and hash(kw) == hash(value)


def test_env():
    env = Env()
    test1 = Symbol('test1')
    test2 = Symbol('test2')
    env[test1] = 1
    env[test2] = 2
    assert len(env) == 2
    assert list(iter(env)) == ["test1", "test2"]
    # del env[test1]
    # assert test1 not in env
    assert env.find(test1) == 1

    outer_key = Symbol('outer_key')

    env.outer = Env()
    env.outer[outer_key] = 10

    with pytest.raises(KeyError):
        env.find(Symbol('N/A'))

    assert env.find(outer_key) == 10
