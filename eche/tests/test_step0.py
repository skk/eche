import pytest

from eche.reader import read_str
from eche.eche_types import Symbol, String


@pytest.mark.parametrize("test_input,expected_cls", [
    (Symbol('abcABC123'), Symbol),
])
def test_parsing_symbol(test_input, expected_cls):
    val = read_str(test_input.value)
    assert isinstance(val, expected_cls) and test_input == val


# noinspection SpellCheckingInspection
@pytest.mark.parametrize("test_input,expected_cls", [
    (String('this is a test.'), String),
    (String('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 {}[]()<>!@#$%^YUI.'),
     String)
])
def test_str_parsing(test_input, expected_cls):
    val = read_str(test_input.value)
    assert isinstance(val, expected_cls) and test_input == val
