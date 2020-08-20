'''Problem 15: Jump Game

https://leetcode.com/problems/jump-game/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
'''


def can_jump(nums):
    '''This algorithm starts at the end position, checking if there is a pair of num + i that will lower the value of the minimum distance.

    A list of nums can reach the last index only if start num can satisfy the minimum distance, lowering the value to 0 to return True.
    '''
    min_distance = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= min_distance:
            min_distance = i
    return min_distance == 0

nums = [1,1,1,0]
expected = True
actual = can_jump(nums)
print(expected == actual)
