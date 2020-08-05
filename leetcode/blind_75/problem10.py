'''
Problem 39. Combination Sum
https://leetcode.com/problems/combination-sum/

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.
'''


def combination_sum(candidates, target):
    if not candidates:
        return 

    result = []

    def dfs(candidates, combination, target, index):
        if target == 0:
            result.append(combination)
            return
        else:
            for i in range(index, len(candidates)):
                if candidates[i] > target:
                    break
                
                dfs(candidates, combination + [candidates[i]], target - candidates[i], i)

    dfs(sorted(candidates), [], target, 0)

    return result


candidates = [2,3,6,7]
target = 7
expected = [
  [2,2,3],
  [7]
]       
actual = combination_sum(candidates, target)
print(expected == actual)