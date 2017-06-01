import pytest

from eche.reader import read_str
from eche.printer import print_str


@pytest.mark.parametrize("test_input", [
    '1',
    '-1',
])
def test_read_atom(test_input):
    assert print_str(read_str(test_input)) == test_input


@pytest.mark.parametrize("test_input", [
    'nil',
])
def test_nil(test_input):
    assert print_str(read_str(test_input)) == test_input


@pytest.mark.parametrize("test_input", [
    'true',
    'false',
])
def test_nil(test_input):
    assert print_str(read_str(test_input)) == test_input


@pytest.mark.parametrize("test_input", [
    '*',
    'abc',
    'abc5',
    'abc-def',
])
def test_eche_type_symbol(test_input):
    assert print_str(read_str(test_input)) == test_input


@pytest.mark.parametrize("test_input", [
    '()',
    '(* 1 2)',
])
def test_eche_type_list(test_input):
    assert print_str(read_str(test_input)) == test_input
