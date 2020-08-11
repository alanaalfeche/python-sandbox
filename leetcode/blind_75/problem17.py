'''
Problem 57. Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
'''

def insert(intervals, new_interval):
    # solution authored by NDW: https://github.com/nolanwrightdev/blind-75-python/blob/master/problems/problem17.py
    L, R = len(intervals), []

    i = 0
    while i < L and intervals[i][1] < new_interval[0]:
        R.append(intervals[i])
        i += 1

    if i < L:
        new_interval[0] = min(new_interval[0], intervals[i][0])

    while i < L and intervals[i][0] <= new_interval[1]:
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    R.append(new_interval)
    R.extend(intervals[i:])
    return R


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_interval = [4,8] # [3,8] 
expected = [[1,2],[3,10],[12,16]]
actual = insert(intervals, new_interval)
print(expected == actual)