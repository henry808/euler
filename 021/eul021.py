#! /usr/bin/python
from __future__ import print_function
from math import sqrt

# Project Euler # 21

def proper_divisors(n):
    results = [1]
    for i in xrange(2, int(sqrt(n))+1):
        if n % i == 0:
            results.append(i)
            if i != n/i:
                results.append(n/i)
    return results

def is_amicable(n):
    a = sum(proper_divisors(n))
    b = sum(proper_divisors(a))
    if b == n and not a == b:
        return True
    else:
        return False

if __name__ == '__main__':
    amicable_sum = 0
    for i in range(3, 10000):
        if is_amicable(i):
            amicable_sum += i
    print(amicable_sum)