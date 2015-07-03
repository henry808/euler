#! /usr/bin/python
from __future__ import print_function
from math import sqrt
# Project Euler #27


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


def consecutive_primes(a, b):
    n = 0
    while is_prime(n ** 2 + a * n + b):
        n += 1
    return n

if __name__ == '__main__':
    max, aa, bb = 0, 0, 0
    for a in range(2001):
        for b in range(2001):
            c_primes = consecutive_primes(a-1000, b-1000)
            if c_primes > max:
                max = c_primes
                aa, bb = a-1000, b-1000
    print(aa * bb)
