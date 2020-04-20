from unittest import mock
from code.dependencies import calculate_area


def test_square():
    result = calculate_area('SQUARE', 2)

    assert result == 4


def test_rectangle():
    result = calculate_area('RECTANGLE', 2, 3)

    assert result == 6


def test_circle_with_proper_pi():
    result = calculate_area('CIRCLE', 2)

    assert result == 12.56636


@mock.patch('code.dependencies.PI', 3)
def test_circle_with_mocked_pi():
    result = calculate_area('CIRCLE', 2)

    assert result == 12


@mock.patch('code.dependencies.rectangle')
def test_circle_with_mocked_rectangle(mocked_rectangle):
    mocked_rectangle.return_value = 12

    result = calculate_area('SQUARE', 2)

    assert result == 12
    mocked_rectangle.assert_called()
