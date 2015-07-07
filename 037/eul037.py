#! /usr/bin/python
from __future__ import print_function
from time import time
from math import sqrt

# Project Euler # 37


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

# these following functions don't work if the
# n has a '0' in it.
def is_prime_ltor(n, direction=1):
    """ n has to be a two or more digit #"""
    shorter = str(n)[1:]
    if is_prime(int(shorter)):
        if len(shorter) < 2:
            return True
        return is_prime_ltor(int(shorter))
    else:
        return False

# duplicate funtion above, but in opposite order
# seperate function for performance issues
def is_prime_rtol(n):
    """ n has to be a two or more digit #"""
    shorter = str(n)[:-1]
    if is_prime(int(shorter)):
        if len(shorter) < 2:
            return True
        return is_prime_rtol(int(shorter))
    else:
        return False

if __name__ == '__main__':
    start_time = time()
    total = 0
    for x in range(11, 999999):
        # can have no 0, 4, 6, or 8 and cannot have 2 or 5 except
        # on the left end (these lines are for performance)
        filter_out = [xx for xx in ['0', '4', '6', '8'] if xx in str(x)]
        filter_out += [xx for xx in ['2', '5'] if xx in str(x)[1:]]
        if len(filter_out) == 0:
            if is_prime(x) and is_prime_ltor(x) and is_prime_rtol(x):
                print(x)
                total += x
    print("total:", total, "  time:", time() - start_time)

