#! /usr/bin/python
from __future__ import print_function

# Project Euler # 15

# this solution goes to each point on the grid and puts the total number
# paths in each cell on the grid (adds the one or two previous points)
# inspired by djikstra's algorithm
def number_routes(width):
    # add 1 because we are looking at edges
    n = width + 1
    table = [[0 for x in range(n)] for x in range(n)]
    table[0][0]=1
    for x in range(n):
        for y in range(n):
            if x - 1 >= 0:
                table[x][y] += table[x - 1][y]
            if y - 1 >= 0:
                table[x][y] += table[x][y - 1]
    return table[n - 1][n - 1]


if __name__ == '__main__':
    print(number_routes(20))