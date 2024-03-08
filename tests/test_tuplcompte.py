from tuplecompte import tuplecount


def test_tuplecount():
    assert tuplecount([1, 2, 3, 4, 5]) == ()
    assert tuplecount([(1, 2, 3), (4, 5), (6, 7, 8, 9)]) == (6, 7, 8, 9)
    assert tuplecount([(1, 2, 3, 4), (5, 6), (7, 8, 9)]) == (1, 2, 3, 4)
