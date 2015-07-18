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
    # find sequence length which is still below max to count down from
    total = 0
    for i in xrange(len(table)):
        total += table[i]
        if total > p:
            break
    max_length = i

    # start from longest possible and then return seq when found
    for length in xrange(max_length, 1, -1):
        for start in range(len(table) - length + 1):
            total = sum(table[start:start+length])
            if total > p:
                break
            if is_prime(total):
                return table[start:start+length]


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

