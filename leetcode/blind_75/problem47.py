'''Problem 47: Contains Duplicate

https://leetcode.com/problems/contains-duplicate/

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''
from collections import Counter


def contains_duplicate(nums):
    '''This algorithm uses counter to build a dictionary using a number in list as key with value as the number of times it appears in the list.
    
    One alternative solution is using set: return not len(set(nums)) == len(nums)
    '''
    counts = Counter(nums)
    for v in counts.values():
        if v > 1: return True
    return False


nums = [1,2,3,1]
expected = True
actual = contains_duplicate(nums)
print(expected == actual)