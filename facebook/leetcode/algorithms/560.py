from typing import List

""" 560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
"""
def subarraySum(nums: List[int], k: int) -> int:
    sum_freq = {}
    sum_freq[0] = 1 # For instance where num in nums = k

    prefix_sums = 0
    k_count = 0

    for num in nums:
        prefix_sums += num
        k_count += sum_freq.get(prefix_sums-k, 0)
        sum_freq[prefix_sums] = sum_freq.get(prefix_sums, 0) + 1     

    return k_count

actual = subarraySum([1,1,1], 2)
expected = 2
assert actual is expected