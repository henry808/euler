#! /usr/bin/python
from __future__ import print_function
from math import ceil, sqrt

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
    results = set()
    for i in xrange(1, int(sqrt(n))+1):
        if n % i == 0:
            results.add(i)
            results.add(n/i)
    return results


def num_divisors(n):
    return len(factor(n))


def divis(n):
    """return first divisor with over n triangles"""
    gen = gen_triangle()
    divisors = 0
    while divisors <= n:
        triangle = gen.next()
        divisors = len(factor(triangle))
    return triangle

if __name__ == '__main__':
    print(divis(500))
