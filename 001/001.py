#! /usr/bin/python
from __future__ import print_function




if __name__ == '__main__':
    sum1 = 0
    for i in range (0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum1 += i
    print(sum1)