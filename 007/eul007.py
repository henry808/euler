#! /usr/bin/python
from __future__ import print_function
from math import sqrt

# Project Euler Problem 7
# find the 10,001st prime number


def is_prime(n):
    """ return True if n is a prime number"""
    if n == 2 | n == 3:
        return True
    if n % 2 == 0 | n % 3 == 0:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def find_prime(nth):
    """find nth place in prime number sequence"""
    count = 1
    number = 2
    while count < nth:
        number += 1
        while not(is_prime(number)):
            number += 1
        count += 1
    return number



if __name__ == "__main__":
    print(find_prime(10001))
