#! /usr/bin/python
from __future__ import print_function
from time import time

# Project Euler # 39

def is_solution(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

def find_solutions(p):
    solutions = []
    for i in range(1, p - 2):
        for j in range(2, p - i - 2):
            k = p - i - j
            # this if statement is for performance
            if k > j and k > i:
                if is_solution(i, j, k):
                    solutions.append((i, j, k))
            else:
                break
    return solutions



if __name__ == '__main__':
    most = 0
    start_time = time()
    for i in range(6, 1000):
        solutions = find_solutions(i)
        if len(solutions) > most:
            most = len(solutions)
            most_solutions = i
        if solutions:
            print("solutions for", i, "are", solutions)
    print("number with most solutions is",
          most_solutions,
          "with",
          most,
          "solutions found in time:",
          time() - start_time)