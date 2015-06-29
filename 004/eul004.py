#! /usr/bin/python
from __future__ import print_function


def ith_digit(n, i=0):
    """returns ith digit of n"""
    return (n/10**i) % 10


def is_palindrome(n):
    """ return true if integer is a plindrome"""
    # calculate length of digits
    length = 0
    n2 = n
    while n2 > 0:
        length += 1
        n2 = n2 / 10
    # check if palindrome
    for i in range(length/2):
        if ith_digit(n, i) != ith_digit(n, length - i - 1):
            return False
    return True

def find_palindromic(n):
    pass