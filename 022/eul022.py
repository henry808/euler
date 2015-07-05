#! /usr/bin/python
from __future__ import print_function
import csv

# Project Euler # 22
def letter_value(word):
    return sum(map(lambda x: ord(x) - 64, word))




if __name__ == '__main__':
    with open('p022_names.txt', 'r') as f:
        for row in csv.reader(f):
            names = row
    names.sort()
    score = 0
    for i in names:
        score += (names.index(i) + 1) * letter_value(i)
    print(score)
