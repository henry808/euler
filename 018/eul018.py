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

triangle = [
            [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
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
    

