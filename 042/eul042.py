#! /usr/bin/python
from __future__ import print_function
from time import time
from math import sqrt
import csv


# Project Euler # 42
def word_value(word):
    return sum(map(lambda x: ord(x) - 64, word))


# Since an integer x is triangular if and only if 8x + 1 is a square
def is_triangle(x):
    return sqrt(8 * x + 1).is_integer()


if __name__ == '__main__':
    start = time()
    with open('words.txt', 'r') as f:
        for row in csv.reader(f):
            names = row

    print("Total score:",
          len([x for x in map(word_value, names) if is_triangle(x)]),
          "found in",
          time() - start,
          "seconds.")
