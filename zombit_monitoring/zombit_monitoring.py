#! /usr/bin/python
from __future__ import print_function


# solution
def answer(intervals):
    intervals = sorted(intervals)
    collapsed = []
    start = intervals[0][0]
    end = intervals[0][1]
    for i in intervals:
        # if break then append interval and start again
        if end < i[0]:
            collapsed.append((start, end))
            start = i[0]
            end = i[1]
        # else join the intervals
        else:
            end = max([end, i[1]])
    # append the current interval 
    collapsed.append((start, end))
    return sum([i[1] - i[0] for i in collapsed])