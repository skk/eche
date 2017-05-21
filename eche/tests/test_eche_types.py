import pytest

from eche_types import Symbol, Atom, Nil, Boolean


@pytest.mark.parametrize("test_input", ['sym1'])
def test_symbol(test_input):
    """
    Test Symbol class.

    Args:
        test_input

    """
    assert Symbol(test_input).value == test_input


@pytest.mark.parametrize("test_input", ['atom1', 1])
def test_atom(test_input):
    """
    Test Atom class.

    Args:
        test_input

    """
    assert Atom(test_input).value == test_input


@pytest.mark.parametrize("test_input", ['atom1', 1])
def test_atom_is_atom(test_input):
    """
    Test Atom class.

    Args:
        test_input

    """
    atom = Atom(test_input)
    assert Atom.is_atom(atom)


@pytest.mark.parametrize("test_input", [None])
def test_nil_is_nil(test_input):
    """
    Test Atom class.

    Args:
        test_input

    """
    nil = Nil(test_input)
    assert Nil.is_nil(nil)


@pytest.mark.parametrize("test_input", [True, False])
def test_boolean_is_boolean(test_input):
    """
    Test Boolean class.

    Args:
        test_input

    """
    boolean = Boolean(test_input)
    assert Boolean.is_boolean(boolean)
