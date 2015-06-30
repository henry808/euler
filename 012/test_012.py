from eul012 import gen_triangle


def test_gen_triangle():
    expected = [1, 3, 6, 10, 15, 21, 28]
    gen = gen_triangle()
    for i in range(len(expected)):
        assert(gen.next() == expected[i])
