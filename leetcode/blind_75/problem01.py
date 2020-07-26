from typing import List
"""Blind Curated 75 - Problem 1: Two Sum 
https://leetcode.com/problems/two-sum/

Given an array of integers, return incides of the two numbers such that they add up to a specific target.

You many assume that each input would have exactly one solution, and you may not use the same element twice.
"""
def brute_force_solution(nums: List[int], target:int) -> List[int]:
    """Iterates through each element x in the list and find value that equals target-x.

    Time Complexity: n^2
    Space Complexity: constant
    Runtime: 3968 ms, faster than 19.97% of Python3 online submissions for Two Sum.
    Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Two Sum.
    """
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target-nums[i]:
                return i, j

print(brute_force_solution([2222222,2222222], 4444444))

# Improved Solution:
def hash_map_solution(nums: List[int], target: int) -> List[int]:
    """Leverage constant lookup of hash map to return the pair
    
    Time Complexity: n for traversing the list
    Space Complexity: n for extra space required for the hash table
    Runtime: 48 ms, faster than 78.72% of Python3 online submissions for Two Sum.
    Memory Usage: 14.2 MB, less than 60.70% of Python3 online submissions for Two Sum.
    """
    targets = {} # {difference: index}
    for index, num in enumerate(nums):
        if num in targets:
            return [targets[num], index]
        targets[target - num] = index

print(hash_map_solution([2,7,11,15], 4444444))
