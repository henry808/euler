#! /usr/bin/python
from __future__ import print_function
from math import sqrt

def prime():
    """Generates prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23...
    """
    n = 1
    while True:
        n += 1
        if not [i for i in range(2, n) if n % i == 0]:
            yield n


def largest_prime(n):
    square_root = int(sqrt(n))
    gen = prime()
    last = 2
    while True:
        next_ = gen.next()
        print(last)
        if next_ > square_root:
            return last
        last = next_


if __name__ == '__main__':
    x = 600851475143
    print(largest_prime(x))
