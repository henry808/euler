#! /usr/bin/python
from __future__ import print_function


def ith_digit(n, i=0):
    """returns ith digit of n"""
    return (n/10**i) % 10


def is_palindrome(n):
    """ return true if integer is a palindrome"""
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


def find_palindromic():
    palindrome = 1
    for i in range(1000):
        for j in range(1000):
            product = i * j
            print(product)
            if is_palindrome(product):
                palindrome = product
    return palindrome


if __name__ == '__main__':
    print(find_palindromic())
