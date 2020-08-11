'''
Problem 16. Merge Intervals
https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.
'''


def merge(intervals):
    # solution authored by NDW: https://github.com/nolanwrightdev/blind-75-python/blob/master/problems/problem17.py
    if not intervals:
        return []
    '''
    Sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).
    Passing lambda as key parameter creates an anonymous fn that is applied to each list item.
    The expression `lambda parameters: expression` yields a function object like a function object defined with:
    def <lambda>(parameters):
        return expression

    https://docs.python.org/3/reference/expressions.html#lambda
    '''
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
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