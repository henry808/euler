from eul009 import is_pythagorean_triplet

def test_is_pythagorean_triplet():

    input_true = [(3,4,5)]
    input_false = [(3, 2, 1), (1, 2, 3)]
    for i in input_false:
        assert(is_pythagorean_triplet(*i) is False)
    for i in input_true:
        assert(is_pythagorean_triplet(*i) is True)