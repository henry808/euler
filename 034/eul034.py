#! /usr/bin/python
from __future__ import print_function

# Project Euler # 34
Factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def is_special(n):
    """returns true if number is equal to the sum of
    its digits each factorialed"""
    nums = list(str(n))
    nums = map(int, nums)
    total = sum(map(lambda x: Factorials[x], nums))
    return n == total

if __name__ == '__main__':
    total = 0
    for i in range(10, Factorials[9] * 7):
        if is_special(i):
            print(i)
            total += i
    print('total:', total)
