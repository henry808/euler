from eul049 import is_permutation


def test_is_permutation():
    inputs_true = [(12, 21), (123, 321), (1234, 1324)]
    inputs_false = [(12, 13), (12, 321), (321, 23)]
    for i in inputs_true:
        assert(is_permutation(*i) is True)
    for i in inputs_false:
        assert(is_permutation(*i) is False)
