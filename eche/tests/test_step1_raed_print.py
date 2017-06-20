import pytest

from eche.tests import print_str_and_read_str_wrapper
from eche.reader import read_str, Blank
from eche.reader import keyword_prefix
from eche.eche_types import Keyword


@pytest.mark.parametrize("test_input", [
    '1',
    '-1',
    '0'
])
def test_number_int(test_input):
    assert print_str_and_read_str_wrapper(test_input)


@pytest.mark.parametrize("test_input", [
    '1.0',
    '1.2543534',
    '5254.47318209'
])
def test_number_float(test_input):
    assert print_str_and_read_str_wrapper(test_input)


@pytest.mark.parametrize("test_input", [
    '*',
    '+',
    'abc',
    'test1',
    'abc-def',
])
def test_eche_type_symbol(test_input):
    assert print_str_and_read_str_wrapper(test_input)


@pytest.mark.parametrize("test_input", [
    '(9 8)',
    '()',
    '(* 1 2)',
    '(+ (* 1 5) (/ 1 0))'
])
def test_eche_type_list(test_input):
    assert print_str_and_read_str_wrapper(test_input)


@pytest.mark.parametrize("test_input", [
    'nil',
])
def test_nil(test_input):
    assert print_str_and_read_str_wrapper(test_input)


@pytest.mark.parametrize("test_input", [
    'true',
    'false',
])
def test_bool(test_input):
    assert print_str_and_read_str_wrapper(test_input)


@pytest.mark.parametrize("test_input", [
    '(1 2, 3,,,,,),,,'
])
def test_whitespace(test_input):
    assert print_str_and_read_str_wrapper(test_input, '(1 2 3)')


@pytest.mark.parametrize("test_input", [
    ':kw',
    '[:kw1 :kw2 :kw3]',
])
def test_keywords(test_input):
    assert print_str_and_read_str_wrapper(test_input)


@pytest.mark.parametrize("test_input", [
    '[0 1 2 3]',
])
def test_vector(test_input):
    assert print_str_and_read_str_wrapper(test_input)


@pytest.mark.parametrize("test_input", [
    '{"abc" 1}',
])
def test_dicts(test_input):
    assert print_str_and_read_str_wrapper(test_input)


@pytest.mark.parametrize("test_input", [
    '(hash-map :key1 1 :key1 2)',
])
def test_hashmap(test_input):
    assert print_str_and_read_str_wrapper(test_input)


@pytest.mark.parametrize("test_input", [
    '; this is a comment!',
])
def test_comments_blank(test_input):
    with pytest.raises(Blank):
        read_str(test_input)


@pytest.mark.parametrize("test_input,expected", [
    ('(1 2) ; another comment!', '(1 2)')
])
def test_comments(test_input, expected):
    assert print_str_and_read_str_wrapper(test_input, expected)


@pytest.mark.parametrize("test_input,expected", [
    (f"{keyword_prefix}KEY", Keyword('KEY')),
])
def test_keyword(test_input, expected):
    assert print_str_and_read_str_wrapper(test_input, expected)


# TODO - add tests for:
# * read of ^/metadata
# * read of @/deref
