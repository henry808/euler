from eul035 import are_rotations_primes


def test_are_rotations_primes():
    inputs_true = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
    inputs_false = [4, 6, 8, 9, 10, 19, 23, 29]
    for i in inputs_true:
        assert(are_rotations_primes(i) is True)
    for i in inputs_false:
        assert(are_rotations_primes(i) is False)