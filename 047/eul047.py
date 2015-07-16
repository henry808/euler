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

# does not return the number of each prime factors because
# not needed to solve this problem (and simplifies problem)
def prime_factors(n, primes):
    """primes is a list of prime numbers that is > n or else
    this function will not work. This functino returns all prime
    factors of n not including duplicates"""
    if n in primes:
        return []
    factors = []
    for num in range(2, n):
        if n % num == 0:
            factors.append(num)
            n = n / num
            # remove duplicates
            while n % num == 0:
                n = n / num
            if n == 1:
                break
            if n in primes:
                factors.append(n)
                break
    return factors


if __name__ == '__main__':
    primes = sieve_of_eratosthenes(9999)
    for i in range(10, 99 - 1):
        if len(prime_factors(i, primes)) == 2:
            # if one prime is found then its possible there are
            # consecutive primes
            possible = True
            print("possible prime:", i)
            for j in range(i + 1, i + 2):
                print("test prime:", j)
                if len(prime_factors(j, primes)) != 2:
                    possible = False
            if possible:
                break
    print(i)



