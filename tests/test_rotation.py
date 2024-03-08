from rotation import rotateList


def test_rotateList():
    assert rotateList([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotateList([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]
    assert rotateList([1, 2, 3, 4, 5], 4) == [2, 3, 4, 5, 1]
    assert rotateList([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]
