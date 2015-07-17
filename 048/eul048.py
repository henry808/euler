#! /usr/bin/python
from __future__ import print_function
from time import time


# Project Euler # 48
def last_digits(n):
    total = 0
    for i in range(1, n + 1):
        x = 1
        for j in range(i):
            x *= i
            x = x % 10000000000
        total += x
    return total % 10000000000


if __name__ == '__main__':
    start = time()
    print("Last ten digits:", last_digits(999), "in time", time() - start)
