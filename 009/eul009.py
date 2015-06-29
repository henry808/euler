#! /usr/bin/python
from __future__ import print_function

# Project Euler # 9


def is_pythagorean_triplet(a, b, c):
    if not(a < b < c):
        return False
    if a ** 2 + b ** 2 == c ** 2:
        return True
    return False


def find_triplet():
    for i in range(998 + 1):
        for j in range(1000-i + 1):
            k = 1000-i-j
            # print(str(i) + " " + str(j) + " " + str(k))
            if is_pythagorean_triplet(i, j, k):
                return i * j * k


if __name__ == '__main__':
    print(find_triplet())