#! /usr/bin/python
from __future__ import print_function
from time import time

# Project Euler # 38

def get_pandigitals(n):
    count = 1
    result = 0
    pandigitals = []
    while result < 987654321:
        # add min value for performance (that way we can skip
        # the inner if statement if the number is below smallest
        # legal number)

        # this checks if it is a pandigital:
        if 123456789 - 1 < result < 987654321 + 1:
            if all([str(g) in str(result) for g in range(1, 10)]):
                pandigitals.append(result)
        # check next series up to count to get next result
        count += 1
        total = ''
        for i in range(1, count):
            number = str(n * i)
            total += number
        result = int(total)
    return pandigitals


if __name__ == '__main__':
    start_time = time()
    biggest = 0
    # first digit must be 9 and 4 or less digits because five digit
    # number x2 is too large
    for i in xrange(9, 9876):
        pandigital = get_pandigitals(i)
        if pandigital:
            biggest = max([biggest, max(pandigital)])
        if pandigital:
            print('for ', i, "pandigital:", pandigital)
    print("found largest:", biggest, "in time: ", time() - start_time)
