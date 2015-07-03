#! /usr/bin/python
from __future__ import print_function

# Project Euler #26


def get_cycle_len(d):
    """ """
    for t in range(1, d):
        if 1 == 10**t % d:
            return t


if __name__ == '__main__':
    biggest_cycle = 0
    for i in range(2, 1000):
        print(i, "  ", get_cycle_len(i))
        if get_cycle_len(i) > biggest_cycle:
            biggest_cycle = get_cycle_len(i)
            biggest_cycle_num = i
    print(biggest_cycle_num)
