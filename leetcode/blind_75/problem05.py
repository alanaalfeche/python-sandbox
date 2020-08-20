'''Problem 5: 3Sum

https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 

Find all unique triplets in the array which gives the sum of zero.
'''


def three_sum(nums):
    '''Original: https://stackoverflow.com/a/59534168
    
    This solution uses a nested sliding window in a for-loop. The i variable in for-loop will act as one of the addends and the sliding window will return the other two addends.   
    '''

    # edge case: list is less than 3 so a tuplet would be invalid
    if len(nums) < 3:
        return []

    # edge case: arrays of zeroes
    elif sum([i**2 for i in nums]) == 0:
        return [[0] * 3]

    nums.sort()
    result = []
    for i in range(len(nums)):
        # skip i duplicates
        if nums[i] == nums[i-1]:
            continue

        l, r = i+1, len(nums)-1
        while l < r:
            if nums[l] + nums[r] + nums[i] < 0:
                l += 1
            elif nums[l] + nums[r] + nums[i] > 0:
                r -= 1
            else:
                result.append([nums[i],nums[l],nums[r]])
                l += 1
                # skip output duplicates
                while l < r and nums[l] == nums[l-1]:
                    l += 1

    return result


nums = [-1,0,1,2,-1,-4]
expected = [[-1, -1, 2], [-1, 0, 1]]
actual = three_sum(nums)
print(expected == actual)