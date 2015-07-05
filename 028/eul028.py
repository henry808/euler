#! /usr/bin/python
from __future__ import print_function
from pprint import pprint
from numpy import ndarray, fliplr, flipud, rot90

# Project Euler #28

SIZE = 1001

grid = ndarray(shape=(SIZE, SIZE), dtype=int)
grid.fill(0)

if __name__ == '__main__':
    x = y = middle = len(grid) / 2
    counter = 0
    for i in range(SIZE * SIZE):
        if(i % SIZE == 0):
            print(i)
        counter += 1
        # 2d arrays are flipped in python
        grid[x][y] = counter
        # advance to next square
        if SIZE - 1 == x + y and x >= middle:
            x += 1
        # on right side, and between diagnals, move down
        elif (x > middle and
              SIZE - x - 1 < y <= x - 1):
            y += 1
        # on bottom, move left
        elif (y > middle and
              SIZE - y - 1 < x <= y):
            x -= 1
        # on left side, and between diagnals, move up
        elif (x < middle and
              x < y <= SIZE - x - 1):
            y -= 1
        # top move right    
        else:
            x += 1
    total = 0
    for x in range(SIZE):
        total += grid[x][x]
        total += grid[x][SIZE - x - 1]
    total -= grid[middle][middle]
    print("total:", total)
    pprint(flipud(rot90(grid)))
