from typing import List
"""
Problem 5: 3Sum
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""
def two_for_loop(nums: List[int]) -> List[List[int]]:
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

def three_for_loop(nums):
    result = []
    for i in range(0, len(nums)-2):
        for j in range(i + 1, len(nums)-1):
            for k in range(j + 1, len(nums)):
                if not sum([nums[i], nums[j], nums[k]]):  # 0 is False
                    result.append([nums[i], nums[j], nums[k]])

    return result

def while_loop(nums):
    result = []
    nums.sort() # kinda cheating
    r = len(nums)-1
    for i in range(len(nums)-2):
        l = i + 1
        while (l < r):
            tsum = nums[i] + nums [l] + nums [r]
            if (tsum < 0):
                l += 1
            if (tsum > 0):
                r -= 1
            if (tsum == 0):
                result.append([nums[i], nums[l], nums[r]])
                l += 1
    
    # sorted makes this work 
    unique_lst = []
    [unique_lst.append(sublst) for sublst in result if not unique_lst.count(sublst)]

    return unique_lst

def a_solution(nums):
    """
    Runtime: 1768 ms, faster than 20.89% of Python3 online submissions for 3Sum.
    Memory Usage: 17.2 MB, less than 64.20% of Python3 online submissions for 3Sum.
    Original: https://stackoverflow.com/a/59534168
    """
    # edge case: list is less than 3 so a tuplet would be invalid
    if len(nums)<3:
        return []

    # edge case: arrays of zeroes
    elif sum([i**2 for i in nums]) == 0:
        return [[0] * 3]

    nums.sort()
    result = []
    for i in range(len(nums)):
        # skip duplicates
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l, r = i+1, len(nums)-1
        while l < r:
            _sum = nums[l] + nums[r]
            if _sum + nums[i] < 0:
                l += 1
            elif _sum + nums[i] > 0:
                r -= 1
            else:
                result.append([nums[i],nums[l],nums[r]])
                l += 1
                # skip duplicates
                while l < r and nums[l] == nums[l-1]:
                    l += 1

    return result

print(two_for_loop([-1, 0, 1, 2, -1, -4])) # Fail. Wrong Answer. 
# [[-1, 0, 1], [-1, 1, 0], [-1, 2, -1], [-1, -1, 2], [0, 1, -1], [0, -1, 1], [1, -1, 0], [2, -1, -1], [2, -4, 2]]
print(three_for_loop([-1, 0, 1, 2, -1, -4])) # Fail. Wrong Answer. 
# [[-1, 0, 1], [-1, 2, -1], [0, 1, -1]]
print(while_loop([-1,0,1,2,-1,-4])) # Fail. 82/313 test cases passed.
# [[-1, -1, 2], [-1, 0, 1]]
print(a_solution([-1,0,1,2,-1,-4])) # Pass.
# [[-1, -1, 2], [-1, 0, 1]]