#! /usr/bin/python
from __future__ import print_function

# Project Euler # 20

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def add_digits(n):
    return sum(map(int, list(str(n))))

if __name__ == '__main__':
    print(add_digits(factorial(100)))

