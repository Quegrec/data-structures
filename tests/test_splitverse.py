from splitverse import splitverse
mrd = "Python est un language."


def test_split_debut():
    assert splitverse.split_debut(mrd) == "Python + est un language."


def test_split_fin():
    assert splitverse.split_fin(mrd) == "Python est un + language."


def test_reverse():
    assert splitverse.reverse(mrd) == ".egaugnal nu tse nohtyP"


def test_reversed():
    assert splitverse.reversed(mrd) == ["language.", "un", "est", "Python"]
