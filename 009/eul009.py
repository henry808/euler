#! /usr/bin/python
from __future__ import print_function

# Project Euler # 9

def is_pythagorean_triplet(a, b, c):
    if not(a < b < c):
        return False
    if a ** 2 + b ** 2 == c ** 2:
        return True
    return False
