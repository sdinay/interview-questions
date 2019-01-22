from reverse_int import reverse_int


def test_negative():
    result = reverse_int(-123)
    assert result == -321


def test_zero():
    result = reverse_int(0)
    assert result == 0


def test_positive():
    result = reverse_int(9876)
    assert result == 6789


def test_max_overflow():
    input = 2**31 - 1
    result = reverse_int(input)
    result == 0

def test_min_overflow():
    input = -2**31
    result = reverse_int(input)
    result == 0
