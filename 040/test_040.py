from eul040 import find_nth_digit


def test_find_nth_digit():
    expected = 123456789101112131415161718192021
    result = ''
    for i in range(1, len(str(expected)) + 1):
        result += find_nth_digit(i)
    assert(int(result) == expected)
