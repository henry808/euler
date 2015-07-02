from eul025 import fibonacci


def test_fibonacci():
    expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    gen = fibonacci()
    for i in range(len(expected)):
        assert (gen.next() == expected[i])
