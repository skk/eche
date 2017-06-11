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
    a = read_str(test_input)
    assert print_str(a) == test_input


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


@pytest.mark.parametrize("test_input", [
    '(1 2, 3,,,,,),,,'
])
def test_whitespace(test_input):
    a = read_str(test_input)
    b = print_str(a)
    assert str(a) == b


@pytest.mark.parametrize("test_input", [
    ':kw',
    '[:kw1 :kw2 :kw3]',
])
def test_keywords(test_input):
    assert print_str(read_str(test_input)) == test_input


@pytest.mark.parametrize("test_input", [
    '[0 1 2 3]',
])
def test_vector(test_input):
    actual = print_str(read_str(test_input))
    excepted = test_input
    assert actual == excepted


@pytest.mark.parametrize("test_input", [
    '{"abc" 1}',
])
def test_dicts(test_input):
    a = read_str(test_input)
    b = test_input
    assert print_str(a) == b
