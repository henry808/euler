from eul032 import is_pandigital


def test_is_pandigital():
    input_true = ['1', '1234', '4321', '192837465']
    input_false = ['0', '10', '2', '9', '13', '31', '9876543210']
    for i in input_true:
        assert(is_pandigital(i) is True)
    for i in input_false:
        assert(is_pandigital(i) is False)