'''Problem 1: Two Sum 

https://leetcode.com/problems/two-sum/

Given an array of integers, return incides of the two numbers such that they add up to a specific target.

You many assume that each input would have exactly one solution, and you may not use the same element twice.
'''


def two_sum(nums, target):
    '''If the num is available in visited, then it is the pair addend of the current num.'''
    visited = {} # {diff: index}
    for index, num in enumerate(nums):
        if num in visited:
            return [visited[num], index]
        visited[target - num] = index


nums = [2,7,11,15]
target = 9
expected = [0, 1]
actual = two_sum(nums, target)
print(expected == actual)