from minmaj import majmin


# def test_majmin_basic():
#     assert majmin("Test String") == "2 majuscules, 9 minuscules"


def test_majmin_empty():
    assert majmin("") == "0 majuscules, 0 minuscules"


def test_majmin_all_uppercase():
    assert majmin("UPPER") == "5 majuscules, 0 minuscules"


def test_majmin_all_lowercase():
    assert majmin("lower") == "0 majuscules, 5 minuscules"


def test_majmin_no_letters():
    assert majmin("1234!@#$") == "0 majuscules, 0 minuscules"


def test_majmin_mixed_characters():
    assert majmin("123 Ab!@#cD") == "2 majuscules, 2 minuscules"
