from inverse import inverse


def test_inverse():
    assert inverse([(1, 2), (3, 4, 5)]) == [(2, 1), (5, 4, 3)]
