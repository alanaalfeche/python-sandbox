from typing import List

"""560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k,
return the total number of continuous subarrays whose sum equals to k.
"""
def subarraySum(nums: List[int], k: int) -> int:
    sum_freq = {}
    sum_freq[0] = 1 # For instance where num in nums = k

    cum_sum = 0
    k_count = 0

    for num in nums:
        cum_sum += num
        k_count += sum_freq.get(cum_sum-k, 0)
        sum_freq[cum_sum] = sum_freq.get(cum_sum, 0) + 1     

    return k_count

assert subarraySum([1,1,1], 2) == 2
