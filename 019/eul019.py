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

def days_in_months(month, year):
    # return days in month from 1 to 12
    if month is 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    months = [31, 0, 31, 30, 31, 30,
              31, 31, 30, 31, 30, 31]
    return months[month - 1]

def count_sundays():
    # Sundays that fall on the 1st of the month:
    # 1 Jan 1901 to 31 Dec 2000
    # first is first of month and 1 = Monday 
    # and 7 = Sunday 
    day = 2 # this has to be set to first day of first mo
    sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if day % 7 == 0:
                sundays += 1
            day += days_in_months(month, year)
    return sundays

if __name__ == '__main__':
    print(count_sundays())


