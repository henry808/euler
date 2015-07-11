#! /usr/bin/python
from __future__ import print_function
from math import sqrt
from time import time

# Project Euler # 40


def is_pandigital(n):
    length = len(str(n))
    if length > 9:
        return False
    digits = map(int, set(n))
    if len(digits) != length or 0 in digits:
        return False
    for digit in digits:
        if digit > length:
            return False
    return True


def is_prime(n):
    """ return True if n is a prime number"""
    if n < 2:
        return False
    if n == 2 | n == 3:
        return True
    if n % 2 == 0 | n % 3 == 0:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    pandigital_primes = []
    start = time()
    # the largest pandigital prime is most likely 9 digits
    # so we should look between 123456789 and 987654321
    # this checks if it is a pandigital:
    for i in xrange(123456789, 987654322, 2):
        length = len(str(i))
        if all([str(g) in str(i) for g in range(1, length + 1)]):
            print(i)
            if is_prime(i):
                pandigital_primes.append(i)
                print(i)
    print("greatest pandigital prime is", max(pandigital_primes),
          "in time:", time() - start)