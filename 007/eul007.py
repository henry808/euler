#! /usr/bin/python
from __future__ import print_function
from math import sqrt

# Project Euler Problem 7
# find the 10,001st prime number


def is_prime(n):
    """ return True if n is a prime number"""
    if n == 2 | n == 3:
        return True
    for i in range(3, int(sqrt(n))/4):
        if n % (i * 4) == 0:
            return False
    return True
