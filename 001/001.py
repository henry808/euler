#! /usr/bin/python
from __future__ import print_function


def multsof3and5_slow():
    """This is the O(n) solution."""
    sum1 = 0
    for i in range (0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum1 += i
    return sum1


def sum_sequence(first, last, number):
    """returns sum of all in a sequence of numbers
    given first and last number
    """
    return (number / 2.0) * (first + last)


def multsof3and5_fast():
    """This is the O(1) solution."""
    sum_of_threes = sum_sequence(3, 999, 999/3)
    sum_of_fives = sum_sequence(5, 995, 995/5)
    sum_of_fifteens = sum_sequence(15, 990, 990/15)
    return int(sum_of_threes + sum_of_fives - sum_of_fifteens)


if __name__ == '__main__':
    print(multsof3and5_slow())
    print(multsof3and5_fast())
