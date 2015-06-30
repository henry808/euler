#! /usr/bin/python
from __future__ import print_function

# Project Euler # 10

# using sieve of Eratosthenes to solve this

def sieve_of_eratosthenes(n):
    array = []
    for i in range(n):
        array.append(True)
    for i in range(2, int(sqrt(n))):

    return array



if __name__ == "__main__":
    print(sieve_of_eratosthenes(10))