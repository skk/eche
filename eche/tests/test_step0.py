import pytest

from eche.reader import read_str
import eche.eche_types


@pytest.mark.parametrize("test_input,expected_cls", [
    ('abcABC123', eche.eche_types.Symbol),
])
def test_parsing_symbol(test_input, expected_cls):
    val = read_str(test_input)
    assert expected_cls(test_input) == val


# noinspection SpellCheckingInspection
@pytest.mark.parametrize("test_input,expected_cls", [
    ('\"this is a test.\"', eche.eche_types.String),
    ('\"abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789{}[]()<>!@#$%^Y.\"',
     eche.eche_types.String)
])
def test_str_parsing(test_input, expected_cls):
    val = read_str(test_input)
    assert expected_cls(test_input) == val
