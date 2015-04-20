
from eul003 import is_prime


def test_is_prime():
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    not_prime = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22]
    for n in prime:
        assert is_prime(n) is True
    for n in not_prime:
        assert is_prime(n) is False
