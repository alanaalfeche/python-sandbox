'''
Problem 39. Combination Sum
https://leetcode.com/problems/combination-sum/

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.
'''


def combination_sum(candidates, target):
    result = []

    def helper(arr, combo, total, target, start):
        if total > target:
            return 
        elif total == target:
            result.append(combo)
            return
        else:
            for i in range(start, len(arr)):
                helper(arr, combo + [arr[i]], total + arr[i], target, i)

    helper(sorted(candidates), [], 0, target, 0)
    return result

candidates = [2,3,6,7]
target = 7
expected = [
  [2,2,3],
  [7]
]       
actual = combination_sum(candidates, target)
print(expected == actual)