from typing import List
"""
Problem 5: 3Sum
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""
def all_tuple_combo_solution(nums: List[int]) -> List[List[int]]:
    """Returns all combination of list to return a tuple of zero.

    Let a + b + c = 0 and a + b = d
    Thus, d + c = 0 or d = 0 - c

    To determine a and b, we can traverse the list to see if there exists a tuple such that
    b = d - a

    Time Complexity: n^2
    Space Complexity: constant
    """

    sol_set = []
    for c in range(0, len(nums)):
        d = 0 - nums[c]
        for a in range(c+1, len(nums)):
            b = d - nums[a]
            if b in nums:
                sol_set.append([nums[c], nums[a], b])
    return sol_set

print(all_tuple_combo_solution([-1, 0, 1, 2, -1, -4]))


