from eul010 import sieve_of_eratosthenes


def test_sieve_of_eratosthenes():
    list1 = sieve_of_eratosthenes(20)
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    for ind, val in enumerate(list1):
        assert (val == expected[ind])
    assert(len(list1) == 8)

def test_sieve_of_eratosthenes():
    list1 = sieve_of_eratosthenes(19)
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    for ind, val in enumerate(list1):
        assert (val == expected[ind])
    assert(len(list1) == 8)