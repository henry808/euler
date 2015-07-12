from eul044 import is_pentagonal

def test_is_pentagonal():
    inputs_true = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
    inputs_false = [2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 116, 118]
    for i in inputs_true:
        assert(bool(is_pentagonal(i)) is True)
    for i in inputs_false:
        assert(is_pentagonal(i) is False)