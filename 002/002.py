#! /usr/bin/python
from __future__ import print_function


def fib():
    """Generates numbers in a fibonacci sequence: f(n) = f(n-1) + f(n-2)
    """
    n = 1
    m = 0
    while True:
        sum = n + m
        m = n
        n = sum
        yield m


if __name__ == '__main__':
    g = fib()
    for i in range(6):
        print(g.next())
