from typing import List
import heapq

"""215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""
def findKthLargestWithSort(nums: List[int], k: int) -> int:
    # TC: O(n lg n)
    # SC: O(1)
    return sorted(nums)[-k]

nums = [3,2,1,5,6,4]
k = 2
expected = 5
assert findKthLargestWithSort(nums, k) is expected

def findKthLargestWithHeap(nums: List[int], k: int) -> int:
    # TC: O(n lg k)
    # SC: O(k)

    # Why [-1]?
    # Returns len(list) == k so the "kth" largest number is the last element in the list.
    return heapq.nlargest(k, nums)[-1] 

assert findKthLargestWithHeap(nums, k)[-1] is expected