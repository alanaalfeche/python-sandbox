'''Problem 33: Search in Rotated Sorted Array

https://leetcode.com/problems/search-in-rotated-sorted-array/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
'''


def search(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            if target < nums[start] and nums[start] <= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        elif target > nums[mid]:
            if target > nums[end] and nums[end] > nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1 


nums = [4,5,6,7,0,1,2]
target = 0
expected = 4       
actual = search(nums, target)
print(expected == actual)