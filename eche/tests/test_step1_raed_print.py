import pytest

import eche.eche_types


@pytest.mark.parametrize("test_input,expected_cls", [
    ('1', eche.eche_types.Atom),
    ('-1', eche.eche_types.Atom),
])
def test_read_atom(test_input, expected_cls):
    assert expected_cls(test_input) == test_input


@pytest.mark.parametrize("test_input,expected_cls", [
    ('nil', eche.eche_types.Nil),
])
def test_nil(test_input, expected_cls):
    assert expected_cls(test_input) == test_input


@pytest.mark.parametrize("test_input,expected_cls", [
    ('true', eche.eche_types.Boolean),
    ('false', eche.eche_types.Boolean),
])
def test_nil(test_input, expected_cls):
    assert expected_cls(test_input) == test_input


@pytest.mark.parametrize("test_input,expected_cls", [
    ('\"abc\"', eche.eche_types.String),
    ('\"abc (with parents)\"', eche.eche_types.String),
    ('\"abc \"def\"', eche.eche_types.String),
])
def test_eche_type_string(test_input, expected_cls):
    assert expected_cls(test_input) == test_input
