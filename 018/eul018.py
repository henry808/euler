#! /usr/bin/python
from __future__ import print_function

# Project Euler # 18

# a fast and easy way of solving this is by using a list 
# that goes bottom to top summing the max as it goes
triangle = [
            [3],
            [7, 4],
            [2, 4, 6],
            [8, 5, 9, 3]
            ]

def max_count():
    sums = triangle[len(triangle) - 1]
    for i in range(len(triangle) - 2, -1, -1):
        new_sums = []
        # sum up each line
        for j in range(len(sums) - 1):
            max_num = max(sums[j], sums[j + 1])
            new_sums.append(triangle[i][j] + max_num)
        sums = new_sums
    return sums[0]

if __name__ == '__main__':
    print(max_count())
    

