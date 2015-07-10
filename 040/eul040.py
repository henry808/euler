#! /usr/bin/python
from __future__ import print_function
from time import time

# Project Euler # 40

def find_nth_digit(n):
    current = 1
    current_word = str(current)
    for i in xrange(1, n):
        current_word = current_word[1:]
        if current_word is '':
            current += 1
            current_word = str(current)
    return current_word[0]

if __name__ == '__main__':
    start = time()
    product = 1
    for i in range(7):
        product *= int(find_nth_digit(10 ** i))
    print("product:", product, " in time: ", time() - start)


