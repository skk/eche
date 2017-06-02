import pytest

from eche.reader import read_str
from eche.printer import print_str

import math


@pytest.mark.parametrize("test_input", [
    '1',
    '-1',
    '0',
    str(math.pi),
    str(math.e)
])
def test_numbers(test_input):
    assert print_str(read_str(test_input)) == test_input


@pytest.mark.parametrize("test_input", [
    '*',
    '+',
    'abc',
    'test1',
    'abc-def',
])
def test_eche_type_symbol(test_input):
    assert print_str(read_str(test_input)) == test_input


@pytest.mark.parametrize("test_input", [
    '((9 8))',
    '()',
    '(* 1 2)',
    '(+ (* 1 5) (/ 1 0))'
])
def test_eche_type_list(test_input):
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
def test_bool(test_input):
    assert print_str(read_str(test_input)) == test_input


