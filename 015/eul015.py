#! /usr/bin/python
from __future__ import print_function
from time import time

# Project Euler # 15

def count_routes(length, x=0, y=0):
    if x == length and y == length:
        sum = 1
    elif x == length:
        sum = count_routes(length, x, y + 1) + 1
    elif y == length:
        sum = count_routes(length, x + 1, y) + 1
    else:
        sum = count_routes(length, x, y + 1) + 1 + count_routes(length, x + 1, y) + 1
    return sum


def number_routes(n):
    # generate a table where each point matches a vertex of grid
    # table = [[False for x in range(0, n + 1) ] for x in range(0, n + 1)]
    length = n + 1
    return count_routes(length, 0, 0)

if __name__ == '__main__':
    print(number_routes(2))