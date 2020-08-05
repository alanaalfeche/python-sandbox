'''
Problem 13. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''

def max_sub_array(nums):
    best_sum = curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        best_sum = max(curr_sum, best_sum)
    return best_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
expected = 6
actual = max_sub_array(nums)
print(expected == actual)