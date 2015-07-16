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
        for i in range(p, n + 1 , p):
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


# above function too slow so will use a table of prime factors
# and after dividing number, look it up in the table
def prime_factors_table(n):
    primes = sieve_of_eratosthenes(n+1)
    table = [set() for x in range(n + 1)]
    for num in range(2, n+1):
        if num not in primes:
            prime_set = set()
            i = 0
            while primes[i] < num:
                if num % primes[i] == 0:
                    prime_set.add(primes[i])
                    if (num / primes[i]) in primes:
                        new_set = prime_set | set([(num / primes[i])])
                    else:
                        new_set = prime_set | table[num / primes[i]]
                    break
                i += 1
            table[num] = new_set
    return table





if __name__ == '__main__':
    num_primes = 4
    start = time()
    table = prime_factors_table(999999)
    print("Generated prime table.")
    for ind, val in enumerate(table):
        if len(val) == num_primes:
            # if one prime is found then its possible there are
            # consecutive primes
            print("possible:", ind, " => prime factors:", val)
            possible = True
            for j in range(ind + 1, ind + num_primes):
                if len(table[j]) != num_primes:
                    possible = False
            if possible:
                for j in range(ind, ind + num_primes):
                    print(j, " => prime factors:", table[j])
                break
    print("time to solve:", time() - start)


