#! /usr/bin/python

# smallest number evenly divisable by 1 through 20
# numbers that are divisable by another number under 20,
# that other number does not need to be checked, so
# only these need to be checked:

divisables = [7, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def is_evenly_divisable(n):
    for i in divisables:
        if n % i != 0:
            return False
    return True
