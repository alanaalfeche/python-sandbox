from typing import List

""" 88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. 

You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.
"""

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1 = m-1
    p2 = n-1

    for p in range(n+m-1, -1, -1):
        if p2 < 0:
            break

        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -=1

    return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
actual = merge(nums1, 3, nums2, 3)
expected = [1, 2, 2, 3, 5, 6]
print(actual == expected)
