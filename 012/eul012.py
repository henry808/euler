#! /usr/bin/python
from __future__ import print_function

# Project Euler # 12


def gen_triangle():
    counter = 1
    sum1 = 0
    while True:
        sum1 += counter
        counter += 1
        yield sum1
