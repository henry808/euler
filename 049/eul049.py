#! /usr/bin/python
from __future__ import print_function
from time import time
from itertools import permutations


# Project Euler # 49
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


def is_permutation(n, m):
    if tuple(str(n)) in permutations(str(m)):
        return True
    return False


if __name__ == '__main__':
    primes = sieve_of_eratosthenes(9876)
    # remove all without 4 digits
    four_d_primes = filter(lambda x: len(str(x)) == 4, primes)
    # remove all with 0
    four_d_primes = filter(lambda x: '0' not in str(x), four_d_primes)
    for ind, val in enumerate(four_d_primes):
        perms = []
        for i in range(ind + 1, len(four_d_primes)):
            if is_permutation(val, four_d_primes[i]):
                perms.append(four_d_primes[i])
        if len(perms) >= 2:
            for i in perms:
                diff = i - val
                if (i + diff) in perms:
                    print("terms:", 
                          "".join([str(val), str(i), str(i + diff)]))
