import pytest
from code.external import division


def test_int_division():
    assert 4 == division(8, 2)


def test_float_division():
    assert 3.5 == division(7, 2)


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)
