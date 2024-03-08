from bonsetudiants import bonsetudiants


def test_bonsetudiants():
    assert bonsetudiants({"Alice": 16, "Bob": 14, "Charlie": 18}) == ({
        "Alice": 16, "Charlie": 18})
