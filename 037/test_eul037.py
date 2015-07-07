from eul037 import is_prime_ltor, is_prime_rtol


def test_is_prime_ltor():
    inputs_true = [23, 37, 83, 197, 823, 3797]
    inputs_false = [41, 79, 127]
    for i in inputs_true:
        assert(is_prime_ltor(i) is True)
    for i in inputs_false:
        assert(is_prime_ltor(i) is False)


def test_is_prime_rtol():
    inputs_true = [32, 37, 79, 379, 739, 3797]
    inputs_false = [41, 97, 223, 827, 197]
    for i in inputs_true:
        assert(is_prime_rtol(i) is True)
    for i in inputs_false:
        assert(is_prime_rtol(i) is False)