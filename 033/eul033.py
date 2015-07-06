#! /usr/bin/python
from __future__ import print_function
from fractions import Fraction

# Project Euler # 33


def cancellable(num, den):
    """ returns a list of all digits except 0
    that are in both numerator and denominator"""
    numorator = list(str(num).replace('0', ''))
    denominator = list(str(den).replace('0', ''))
    if len(numorator) < 2 or len(denominator) < 2:
        return []
    return map(int, list(set(numorator) & set(denominator)))


def remove_from(num, remove):
    """ only works for 2 digit numbers with no zeroes """
    num = str(num)
    answer = num.replace(str(remove), '')
    if answer == '':
        # if answer is empty, there were two of same # and
        # we need to put one back in
        return int(num[:1])
    else:
        return int(answer)

def is_special_fraction(num, den):
    """ only works on 2 digit numerators and denominators"""
    if len(str(num)) != 2 or len(str(den)) != 2:
        return False
    can = cancellable(num, den)
    # if there are two cancellables, the numbers are either the
    # same (they will evaluate to 1 and be trivial) or else
    # they are opposite 78/87 and will not evaluae to 1 before
    # cancelling, so that means that special fractions have
    # to have only one cancellable value
    if not(len(can) == 1):
        return False
    can_value = can[0]
    new_num = remove_from(num, can_value)
    new_den = remove_from(den, can_value)
    if Fraction(new_num, new_den) == Fraction(num, den):
        return new_num, new_den
    else:
        return False


if __name__ == '__main__':
    product = 1
    for den in range(11, 99):
        for num in range(11, den):
            if not(den % 10 == 0) and not(num % 10 == 0):
                new = is_special_fraction(num, den)
                if new:
                    print(num, "/", den, " = ", new[0], "/", new[1])
                    product *= Fraction(num, den)
    print("product:", product)