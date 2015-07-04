#! /usr/bin/python
from __future__ import print_function


# Project Euler #29

def distinct_terms(a1, a2):
    items = set()
    for a in range(a1, a2 + 1):
        for b in range(a1, a2 + 1):
            items.add(a ** b)
    return(len(items))

if __name__ == '__main__':
    print(distinct_terms(2, 100))