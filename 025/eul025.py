#! /usr/bin/python
from __future__ import print_function
import itertools

# Project Euler #25


def fibonacci():
    """fibonacci sequence generator"""
    a1, a2 = 1, 1
    while True:
        yield a1
        a1, a2 = a2, a1 + a2


def first_w_digits(digits):
    """return index of first fibonacci # digits long"""
    gen = fibonacci()
    counter = 0
    while True:
        n = gen.next()
        counter += 1
        if len(str(n)) == digits:
            return counter

if __name__ == '__main__':
    print(first_w_digits(1000))
