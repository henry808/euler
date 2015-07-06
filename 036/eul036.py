#! /usr/bin/python
from __future__ import print_function
from time import time

# Project Euler # 36


def is_palendromic(n):
    """ tests decimal and binary to see if palendromic both ways"""
    digits = str(n)
    if digits != digits[::-1]:
        return False
    bin_digits = bin(n)[2:]
    if bin_digits != bin_digits[::-1]:
        return False
    return True

if __name__ == '__main__':
    total = 0
    for i in range(1, 1000000):
        if is_palendromic(i):
            total += i
            print(i, bin(i)[2:])
    print('total:', total)

