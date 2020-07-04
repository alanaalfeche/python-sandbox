from typing import List
"""
Problem 26: Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""
def solution(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: constant
    Runtime: 80 ms, faster than 90.86% of Python3 online submissions for Remove Duplicates from Sorted Array.
    Memory Usage: 14.4 MB, less than 98.36% of Python3 online submissions for Remove Duplicates from Sorted Array.
    """
    if len(nums) == 0:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    return i + 1

print(solution([0,0,1,1,1,2,2,3,3,4]))