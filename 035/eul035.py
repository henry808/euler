#! /usr/bin/python
from __future__ import print_function
from math import sqrt
from time import time

# Project Euler # 35


def is_prime(n):
    """returns True if n is a prime #
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    square_root = int(sqrt(n))
    if [i for i in range(2, square_root + 1) if n % i == 0]:
        return False
    else:
        return True


def are_rotations_primes(p):
    str_p = str(p)
    # this filter line significanty decreases time
    # by more than 4x
    if '0' in str_p or '5' in str_p:
        return False
    for i in range(len(str_p)):
        str_p = str_p[1:] + str_p[:1]
        if not(is_prime(int(str_p))):
            return False
    return True

if __name__ == '__main__':
    start_time = time()
    # start with 2 because of special cases of 2 and 5 that 
    # this algorithm doesn't find
    count = 2
    # only do odd numbers halves time
    for i in range(1, 1000000, 2):
        if are_rotations_primes(i):
            print(i)
            count += 1
    print('total circular primes: ',
          count,
          " time: ",
          time() - start_time)
