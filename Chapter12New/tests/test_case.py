LIST = [1, 2, 3]


def test_one():
    # Nothing happens
    pass


def test_two():
    assert 2 == 1 + 1


def test_three():
    assert 3 in LIST


def test_fail():
    assert 4 in LIST
