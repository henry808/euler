#! /usr/bin/python
from __future__ import print_function
from time import time
from math import sqrt


# Project Euler # 50
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


def is_prime(n):
    """returns True if n is a prime #
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    square_root = int(sqrt(n))
    if [i for i in range(2, square_root + 1) if n % i == 0]:
        return False
    else:
        return True


def largest_consecutive(p):
    table = sieve_of_eratosthenes(p)
    result = []
    for start in xrange(len(table)):
        total = table[start]
        consecutive_primes = [table[start]]
        for end in xrange(start + 1, len(table)):
            consecutive_primes.append(table[end])
            total += table[end]
            if total > p:
                break
            if is_prime(total) and len(consecutive_primes) > len(result):
                result = consecutive_primes[:]
    return result
if __name__ == '__main__':
    start = time()
    n = largest_consecutive(1000000)
    print("Prime with longest sequence:",
          sum(n),
          "with",
          len(n),
          "terms found in",
          time() - start,
          "seconds.")

