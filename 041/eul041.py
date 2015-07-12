#! /usr/bin/python
from __future__ import print_function
from math import sqrt
from time import time
from itertools import permutations


# Project Euler # 41
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


if __name__ == '__main__':
    # start at greatest
    # 1+2+3+4+5+6+7+8+9=45 => divisable by 3)
    # 1+2+3+4+5+6+7+8=36 => divisable by 3)
    digits = '7654321'
    digits_list = []
    for i in range(len(digits)):
        digits_list.append(digits)
        digits = digits[1:]
    start = time()
    end = False
    for i in digits_list:
        for p in permutations(i):
            current = int("".join(p))
            # only checks odd values for performance
            if current % 2 == 1:
                # print(current)
                if is_prime(int("".join(p))):
                    print("greatest pandigital prime is", 
                          current,
                          "in time:", time() - start)
                    end = True
                    break
        if end is True:
            break
