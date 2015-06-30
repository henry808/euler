#! /usr/bin/python
from __future__ import print_function
from time import time

# Project Euler # 14
# this solution works, but is slow


def generate_sequence(n):
    """generate sequance starting with n"""
    list1 = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        list1.append(n)
    return list1


def longest(b):    
    max1 = 1
    longest1 = 1
    for i in range(1, b + 1):
        # print(generate_sequence(i), "len: ", len(generate_sequence(i)))
        if max1 < len(generate_sequence(i)):
            max1 = len(generate_sequence(i))
            longest1 = i
    return longest1

if __name__ == '__main__':
    start_time = time()
    print(longest(1000000))
    print("time passed: ", time() - start_time)
