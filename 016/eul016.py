#! /usr/bin/python
from __future__ import print_function

# Project Euler # 16

#trivial problem in python

if __name__ == '__main__':
    x = 2 ** 1000
    numbers = list(str(x))
    print(sum(map(int, numbers)))
