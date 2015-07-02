from eul021 import proper_divisors, is_amicable

def test_proper_divisors():
    input = [2, 3, 6, 10, 15, 21, 28]
    expected = [[1], [1], [1, 2, 3], [1, 2, 5],
                [1, 3, 5], [1, 3, 7],
                [1, 2, 14, 4, 7]]
    for ind, val in enumerate(input):
        assert(proper_divisors(val) == expected[ind])

def test_is_amicable():
    assert(is_amicable(220) == True)
    assert(is_amicable(284) == True)