import pytest

from eche.tests import print_str_and_read_str_wrapper
import eche.step0_repl as step


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


@pytest.mark.parametrize("test_input", [
    '(7 8)'
])
def test_read(test_input):
    assert step.READ(test_input) == test_input


@pytest.mark.parametrize("test_input", [
    '(1 2 3)',
    '(+ 1 2)'
])
def test_eval(test_input):
    assert step.EVAL(test_input, None) == test_input


@pytest.mark.parametrize("test_input", [
    '(- 2 3)',
    '(% 1 2)'
])
def test_print(test_input):
    assert step.PRINT(test_input) == test_input


@pytest.mark.parametrize("test_input", [
    '(+ 2 3)',
    '[5 6 7]'
])
def test_rep(test_input):
    assert step.REP(test_input)