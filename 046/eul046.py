#! /usr/bin/python
from __future__ import print_function
from time import time
from math import sqrt


# Project Euler # 46
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


# generator for odd composites
def gen_odd_composite():
    i = 9
    while True:
        yield i
        i += 2
        while is_prime(i):
            i += 2

if __name__ == '__main__':
    start = time()
    gen = gen_odd_composite()
    while True:
        n = gen.next()
        found = False
        for p in range(2, n + 1):
            if is_prime(p):
                end = False
                for s in range(1, int(sqrt(n))):
                    if p + 2 * s ** 2 == n:
                        found = True
                        print(n, "=", p, "+ 2x", s, "|2")
                        end = True
                if end == True:
                    break
        if found is True:
            found = False
        else:
            break
    print("Found:", n, "in time", time() - start)
