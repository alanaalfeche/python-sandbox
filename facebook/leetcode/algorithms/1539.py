from typing import List

"""1539. Kth Missing Positive Number
https://leetcode.com/problems/kth-missing-positive-number/

Given an array arr of positive integers sorted in a strictly increasing order,and an integer k.

Find the kth positive integer that is missing from this array.
"""
def findKthPositiveWithBinarySearch(arr: List[int], k: int) -> int:
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] - mid > k:
            right = mid
        else:
            left = mid + 1
            
    return right + k


def findKthPositiveWithMissingList(arr: List[int], k: int) -> int:
    i, j = 0, 1
    missing = []

    while i < len(arr):
        if arr[i] != j:
            missing.append(j)
            j += 1
        else:
            i += 1
            j += 1
    
    # if-else takes into account input where nothing is missing
    # ex: arr=[1, 2, 3, 4], k=2
    count = len(missing)
    if count < k:
        # k-count takes into account input where the initial subset of arr is missing but not the list itself
        # ex: arr=[5, 6, 7, 8, 9], k=9
        return arr[-1] + k-count
    else:
        return missing[k-1]

expected = 9
actual = findKthPositiveWithMissingList([2, 3, 4, 7, 11], 5)
assert actual is expected


def findKthPositive(arr: List[int], k: int) -> int:
    i, j = 0, 1
    missing = 0

    while i < len(arr):
        if arr[i] != j:
            missing += 1
            if missing == k:
                return j
            j += 1
        else:
            i += 1
            j += 1
    
    return arr[-1] + k-missing

expected = 9
actual = findKthPositive([2, 3, 4, 7, 11], 5)
assert actual is expected