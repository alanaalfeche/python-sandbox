'''Problem 57. Insert Interval

https://leetcode.com/problems/insert-interval/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
'''


def insert(intervals, new_interval):
    '''Authored by NDW: https://github.com/nolanwrightdev/blind-75-python/blob/master/problems/problem17.py
    
    This algorithm starts out by finding entries in the intervals that is not within the range of the new interval. The new interval [i,j] ith term is compared to (lambda intervals: interval) interval[i,j] jth term.

    If the interval j < new_interval i, this means that the interval can be immediately added on the result list. We also have a counter which tracks index i at which this comparison fails. 

    When we hit the failure, we know that an interval might have an ith index that is less than new_interval so we reset the new interval by running min() on new_interval i and interval i. 

    After the reset, we will enter another while loop that mimics the merge interval problem where we seek for interval(~s) ith term that is less than new_interval jth term. 

    Then we perform max() on new_interval j and interval[j], iterating i each time. Once an interval failed to satisfy the case, we exit from the while loop, appending the new_interval to the result list. 

    We also add the remaining of the interval(~s) in the result list. 
    '''
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
new_interval = [4,8]
expected = [[1,2],[3,10],[12,16]]
actual = insert(intervals, new_interval)
print(expected == actual)