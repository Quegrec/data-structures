from somme2nombres import sommeint, sommestr


def test_sommeint():
    assert sommeint("un", "deux") == 3


def test_sommestr():
    assert sommestr("trois", "quatre") == "sept"
