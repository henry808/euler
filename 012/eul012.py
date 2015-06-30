#! /usr/bin/python
from __future__ import print_function

# Project Euler # 12


def gen_triangle():
    """generator generates triangle sequence"""
    counter = 1
    sum1 = 0
    while True:
        sum1 += counter
        counter += 1
        yield sum1


def factor(n):
    """returns a list of factors given n"""
    factors = []
    for i in range(1, n/2):
        if n % i == 0:
            factors.append(i)
    factors.append(n)
    return factors
