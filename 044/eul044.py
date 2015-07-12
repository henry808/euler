#! /usr/bin/python
from __future__ import print_function
from time import time
from math import sqrt


# Project Euler # 44
def is_pentagonal(x):
    if x < 1:
        return False
    n = (sqrt(24 * x + 1) + 1) / 6
    if n.is_integer():
        return n
    else:
        return False


def pentagonal(n):
    return n * (3 * n - 1) / 2

if __name__ == '__main__':
    end = False
    start = time()
    for j in range(1, 10000):
        pj = pentagonal(j)
        for k in range(j + 1, 10000):
            pk = pentagonal(k)
            if is_pentagonal(pk + pj) and is_pentagonal(pk - pj):
                print("j is", j, "k is", k, "D is", pk - pj, "time:", time() - start)
                end = True
                break
        if end:
            break

