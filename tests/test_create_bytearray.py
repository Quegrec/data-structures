from create_bytearray import translate


def test_translate():
    assert translate([1, 2, 3, 4, 5]) == bytearray(b'\x01\x02\x03\x04\x05')
