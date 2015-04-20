#! /usr/bin/python
from __future__ import print_function
from math import sqrt

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


def largest_prime(n):
    square_root = int(sqrt(n))
    for num in range(square_root, 0, -1):
        if not [i for i in range(2, num) if num % i == 0]:
            print(num)
            if n % num == 0:
                return num
    # gen = prime()
    # last = 2
    # while True:
    #     next_ = gen.next()
    #     print(last)
    #     if next_ > square_root:
    #         return last
    #     last = next_


if __name__ == '__main__':
    x = 600851475143
    print(largest_prime(x))
