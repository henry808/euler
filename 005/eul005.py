#! /usr/bin/python
# solution to Project Euler Problem

from numpy import prod

# smallest number evenly divisable by 1 through 20
# numbers that are divisable by another number under 20,
# that other number does not need to be checked, so
# only these need to be checked:

divisables = [7, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# the number has to be divisable by the product of all the primes
# prime and nonprime divisables:
prime_d = [7, 11, 13, 17, 19]
non_d = [12, 14, 15, 16, 18, 20]

# start with product of all primes and then mutiply that by
# a counter until we find a number divisable by all


def is_evenly_divisable(n):
    for i in divisables:
        if n % i != 0:
            return False
    return True


def find_divisable():
    product = prod(prime_d)
    count = 1
    while True:
        if is_evenly_divisable(product * count):
            return product * count
        count += 1

if __name__ == '__main__':
    print(find_divisable())