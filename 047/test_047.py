from eul047 import sieve_of_eratosthenes, prime_factors
from eul047 import prime_factors_table


def test_prime_factors():
    primes = sieve_of_eratosthenes(9999)
    inputs = [2, 3, 4, 10, 12, 15, 16, 17, 20]
    expected = [[], [], [2], [2, 5], [2, 3], [3, 5], [2], [], [2, 5]]
    for ind, val in enumerate(inputs):
        assert(prime_factors(val, primes) == expected[ind])

def test_prime_factors_table():
    n = 10
    results = prime_factors_table(10)
    expected = [set(),
                set(),
                set([2]),
                set([3]),
                set([2]),
                set([5]),
                set([2, 3]),
                set([7]),
                set([2]),
                set([3]),
                set([2, 5])]
    print results
    assert results == expected