#! /usr/bin/python
from __future__ import print_function


def fib():
    """Generates numbers in a fibonacci sequence: f(n) = f(n-1) + f(n-2)
    """
    n = 1
    m = 0
    while True:
        sum = n + m
        m, n = n, sum
        yield m

def all_evens_under(n):
    """generates a list of all evens under n"""
    gen = fib()
    l = []
    while True:
        current = gen.next()
        if current > n:
            return l
        if current % 2 == 0:
            l.append(current)



if __name__ == '__main__':
    print(sum(all_evens_under(4000000)))
