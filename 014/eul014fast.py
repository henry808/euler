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


def generate_sequence_length(n):
    """generate length for sequance starting with n"""
    list1 = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        list1.append(n)
    print("list ", list1, )
    return len(list1)


def generate_sequence_length_table(size):
    """generate table of lengths for sequance of size size"""
    table_lengths = {}
    for current in range(1, size + 1):
        n = current
        current_length = 1
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
            if n in table_lengths:
                current_length += table_lengths[n]
                break
            current_length += 1
        table_lengths[current] = current_length
    return table_lengths


def longest(b):
    table = generate_sequence_length_table(b)
    max_value  = max(table.values())
    for key, val in table.iteritems():
        if val == max_value:
            return key

if __name__ == '__main__':
    start_time = time()
    print(longest(1000000))
    print("time passed: ", time() - start_time)
