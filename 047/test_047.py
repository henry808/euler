from eul047 import sieve_of_eratosthenes, prime_factors


def test_prime_factors():
    primes = sieve_of_eratosthenes(9999)
    inputs = [2, 3, 4, 10, 12, 15, 16, 17, 20]
    results = [[], [], [2], [2, 5], [2, 3], [3, 5], [2], [], [2, 5]]
    for ind, val in enumerate(inputs):
        assert(prime_factors(val, primes) == results[ind])
