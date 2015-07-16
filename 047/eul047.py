#! /usr/bin/python
from __future__ import print_function
from time import time
from math import sqrt


# Project Euler # 47
# using sieve of Eratosthenes to solve this

def sieve_of_eratosthenes(n):
    array = [True] * (n + 1)
    p = 2
    count = 2
    prime_list = []
    while True:
        prime_list.append(p)
        # Make all False that are mutiples of prime
        for i in range(p, n, p):
            array[i] = False
        # Find next prime
        while array[count] is False:
            count += 1
            if count == n:
                # if last # is a prime, need to add it
                if array[count] is True:
                    prime_list.append(count)
                return prime_list
        p = count
if __name__ == '__main__':
    print(sieve_of_eratosthenes(9999))