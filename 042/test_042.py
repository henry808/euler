from eul042 import is_triangle


def test_is_triangle():
    input_true = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    input_false = [2, 4, 5, 7, 8, 9, 11, 12, 13, 14, 16]
    for val in input_true:
        assert(is_triangle(val) is True)
    for val in input_false:
        assert(is_triangle(val) is False)