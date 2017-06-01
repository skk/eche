import pytest

from eche.reader import read_str
from eche.printer import print_str


@pytest.mark.parametrize("test_input", [
    'abcABC123',
])
def test_parsing_symbol(test_input):
    assert print_str(read_str(test_input)) == test_input


# noinspection SpellCheckingInspection
@pytest.mark.parametrize("test_input", [
    '\"this is a test.\"',
    '\"abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789{}[]()<>!@#$%^Y.\"',
])
def test_str_parsing(test_input):
    assert print_str(read_str(test_input)) == test_input
