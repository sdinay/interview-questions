from reverse_int import reverse_int, INT_MAX, INT_MIN


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
    input = 1563847412
    assert input < INT_MAX
    result = reverse_int(input)
    result == 0

def test_min_overflow():
    input = -1563847412
    assert INT_MIN < input
    result = reverse_int(input)
    result == 0
