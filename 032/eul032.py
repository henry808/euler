#! /usr/bin/python
from __future__ import print_function


# Project Euler #32

def is_pandigital(n):
    length = len(str(n))
    if length > 9:
        return False
    digits = map(int, set(n))
    if len(digits) != length or 0 in digits:
        return False
    for digit in digits:
        if digit > length:
            return False
    return True


if __name__ == '__main__':
    # anything over 5000 will automatically result in a higher than
    # 9 digit sum of digits of multiplicand/multiplier/product
    total = set()
    for x in range(0, 5000):
        for y in range(0, 5000):
            z = x * y
            digits = "".join([str(z), str(x), str(y)])
            if len(digits) > 9:
                break
            if len(digits) == 9 and is_pandigital(digits):
                sorted_digits = list(digits)
                sorted_digits.sort()
                digits = "".join(sorted_digits)
                print(x, ' X ', y, ' = ', z)
                total.add(z)
    print("total of all products:", sum(total))

