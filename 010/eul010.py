#! /usr/bin/python
from __future__ import print_function

# Project Euler # 10

# using sieve of Eratosthenes to solve this

def sieve_of_eratosthenes(n):
    array = [True] * n
    p = 2
    count = 2
    prime_list = []
    while True:
        prime_list.append(p)
        # Make all False that are mutiples of prime
        for i in range(0, n, p):
            array[i] = False
        # Find next prime
        while array[count] is False:
            count += 1
            if count == n:
                return prime_list
        p = count

if __name__ == '__main__':
    print(sum(sieve_of_eratosthenes(2000000)))