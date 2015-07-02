#! /usr/bin/python
from __future__ import print_function
import itertools

# Project Euler #24
# may be cheating because I used the permutation function built into itertools

def ith_permutation(seq, ind):
    """ith permutation of seq list"""
    for i, v in enumerate(itertools.permutations(n)):
        if i + 1 == ind: return(v)

if __name__ == '__main__':
    n = [0,1,2,3,4,5,6,7,8,9]
    print("".join(map(str,ith_permutation(n, 1000000))))