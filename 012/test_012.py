from eul012 import gen_triangle, factor, num_divisors


def test_gen_triangle():
    expected = [1, 3, 6, 10, 15, 21, 28]
    gen = gen_triangle()
    for i in range(len(expected)):
        assert(gen.next() == expected[i])


def test_factor():
    input = [1, 3, 6, 10, 15, 21, 28]
    expected = [{1}, {1, 3}, {1, 2, 3, 6}, {1, 2, 5, 10},
                {1, 3, 5, 15}, {1, 3, 7, 21},
                {1, 2, 4, 7, 14, 28}]
    for ind, val in enumerate(input):
        assert(factor(val) == expected[ind])


def test_num_factor():
    inputl = [1, 3, 6, 10, 15, 21, 28]
    expected = [1, 2, 4, 4, 4, 4, 6]
    for ind, val in enumerate(inputl):
        print(val, " ", num_divisors(val))
        assert(num_divisors(val) == expected[ind])
