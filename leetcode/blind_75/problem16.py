'''Problem 16. Merge Intervals

https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.
'''


def merge(intervals):
    # solution authored by NDW: https://github.com/nolanwrightdev/blind-75-python/blob/master/problems/problem17.py
    if not intervals:
        return []
    '''Sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).

    Passing lambda as key parameter creates an anonymous fn that is applied to each list item.

    The expression `lambda parameters: expression` yields a function object like a function object defined with:

    def <lambda>(parameters):
        return expression

    This algorithm start by sorting the intervals on the [i][j] ith term. We then compare the last j value to the start value of an interval [start, end] from our traversal.

    If the start value is less than j, then it can be merged. We then used max function to determine whether we use the j or the end value to fully merge an interval.

    Otherwise, just append start,end to the result. 
    '''
    if not intervals:
        return []

    intervals.sort(key = lambda x: x[0])
    result = [intervals[0]]
    for interval in intervals[1:]:
        start, end = interval
        if start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append(interval)
    return result


intervals = [[1,4],[2,3]]
expected = [[1,4]]
actual = merge(intervals)
print(expected == actual)