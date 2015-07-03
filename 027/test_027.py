from eul027 import consecutive_primes


def test_consecutive_primes():
    expected = 40
    assert(consecutive_primes(1, 41) == expected)