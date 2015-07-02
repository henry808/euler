#! /usr/bin/python
from __future__ import print_function

# Project Euler # 19
# 1/1/1900 is a Monday


def is_leap_year(n):
    # if n is a century
    if n % 100 == 0:
        if n % 400 == 0:
            return True
        else:
            return False
    if n % 4 == 0:
        return True
    else:
        return False

