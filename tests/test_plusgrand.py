from plusgrand import compare


def test_compare():
    assert compare(1, 2, 3) == 3
    assert compare(1, 9, 3) == 9
