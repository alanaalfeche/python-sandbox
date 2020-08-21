'''Problem 198: House Robber

https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''


def rob(houses):
    left, right = 0, 0
    for h in houses:
        left, right = right, max(left + h, right)
    return right


houses = [1,2,3,1]
expected = 4
actual = rob(houses)
print(expected == actual)