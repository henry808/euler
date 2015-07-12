#! /usr/bin/python
from __future__ import print_function
from time import time
from math import sqrt


# Project Euler # 45

# Since an integer x is triangular if and only if 8x + 1 is a square
def is_triangle(x):
    return sqrt(8 * x + 1).is_integer()


def is_pentagonal(x):
    if x < 1:
        return False
    n = (sqrt(24 * x + 1) + 1) / 6
    if n.is_integer():
        return n
    else:
        return False

if __name__ == '__main__':
    start = time()
    # start one higher than H143
    n = 144
    while True:
        Hn = n * (2 * n - 1)
        if is_triangle(Hn) and is_pentagonal(Hn):
            break
        n += 1
    print("TP and H value:", Hn, "in", time() - start, "seconds")
