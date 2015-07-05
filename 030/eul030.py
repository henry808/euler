#! /usr/bin/python
from __future__ import print_function


# Project Euler #30

def sum_powers(n, p):
    """"""
    digits = list(str(n))
    return sum(map(lambda x: x ** p, map(int, digits)))

N = 5

if __name__ == '__main__':
    total = 0
    # highest sum of 5th powers is 354294 fo 6 digit numbers
    # highest sum of 5th powers of 7 digit numbers is 413343,
    # 6 digits only, so only have to test to 354294
    for i in range(2, 354295):
        if i == sum_powers(i, N):
            print(i)
            total += i
    print(total)
