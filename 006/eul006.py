#! /usr/bin/python
from __future__ import print_function


def sqr(x):
    return x ** 2


def sum_squares(n):
    return (sum(map(sqr, range(1, n + 1))))
    # sum1 = 0
    # for i in range(1, n + 1):
    #     sum1 += i**2
    # return sum1


if __name__ == '__main__':
    print(sum_squares(10))
