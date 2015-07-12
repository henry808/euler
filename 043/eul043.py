#! /usr/bin/python
from __future__ import print_function
from time import time
from itertools import permutations


# Project Euler # 43

# only works on 0 to 9 pandigitals:
# (accepts a string or list, not an int)
# reversed sequence and indices for performance boost
seq = [17, 13, 11, 7, 5, 3, 2]
def is_special(n):
    for ind, val in enumerate(seq):
        number = int("".join(n[7 - ind:10 - ind]))
        if number % val != 0:
            return False
    return True


if __name__ == '__main__':
    start = time()
    digits = "0123456789"
    total = 0
    for n in permutations(digits):
        if is_special(n):
            total += int("".join(n))
            print("".join(n))
    print('Total:', total, "and took", time() - start, "seconds.")
