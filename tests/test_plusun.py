from plusun import incr


def test_incr():
    assert incr(
        bytearray(b'\x01\x02\x03')) == bytearray(b'\x02\x03\x04')
