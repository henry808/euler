#! /usr/bin/python
from __future__ import print_function
from math import sqrt

# Project Euler # 23

def proper_divisors(n):
    results = [1]
    for i in xrange(2, int(sqrt(n))+1):
        if n % i == 0:
            results.append(i)
            if i != n/i:
                results.append(n/i)
    return results

if __name__ == '__main__':
    abundant_table = []
    for i in range(2, 28123):
        if sum(proper_divisors(i)) > i:
            abundant_table.append(i)
    # made a set to avoid duplicates and to increase speed
    abundant_sum_table = set()
    for i in range(len(abundant_table)):
        # - i to avoid summing twice
        for j in range(len(abundant_table) - i):
            num = abundant_table[i] + abundant_table[j]
            if num < 28123:
                # if num < 100: print(num)
                abundant_sum_table.add(num)
    # abundant_sum_table.sort()
    total = 0
    non_abundant_sums = []
    for i in range(28123):
        if i not in abundant_sum_table:
            total += i
            non_abundant_sums.append(i)
    non_abundant_sums.sort()
    print(total)