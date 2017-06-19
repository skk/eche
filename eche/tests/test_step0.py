import pytest

from eche.tests import print_str_and_read_str_wrapper


@pytest.mark.parametrize("test_input", [
    'abcABC123',
])
def test_parsing_symbol(test_input):
    assert print_str_and_read_str_wrapper(test_input)


# noinspection SpellCheckingInspection
@pytest.mark.parametrize("test_input", [
    '\"this is a test.\"',
    '\"abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789{}[]()<>!@#$%^Y.\"',
])
def test_str_parsing(test_input):
    assert print_str_and_read_str_wrapper(test_input)
