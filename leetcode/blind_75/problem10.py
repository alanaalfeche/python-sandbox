'''Problem 39: Combination Sum

https://leetcode.com/problems/combination-sum/

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.
'''


def combination_sum(candidates, target):
    ''' 0   1    2       3          4                  5
    1  [ ] [1] [1,1] [1, 1, 1] [1, 1, 1, 1]     [1, 1, 1, 1, 1]
    2  [ ] [ ] [2]   [2, 1]    [2, 2] [2, 1, 1] [2, 1, 1, 1] [2, 2, 1]
    3  [ ] [ ] [ ]   [3]       [3, 1]           [3, 1, 1] [3, 2] 

    All unique combinations are found in the last columns. 
    '''
    # like line 12, we need to create a dp with targets + 1 to account for 0
    dp = [[] for _ in range(target+1)]

    candidates.sort()
    for c in candidates:
        for i in range(1, target+1): # skipping 0 column
            if i < c: continue # it's just an empty list []
            if i == c: dp[i].append([c]) # e.g. i = 3, c = 1 --> dp[3] = 1,1,1 
            else: 
                for _list in dp[i-c]: # e.g i = 5, c = 3 --> 2: [1,1] or [2]
                    dp[i].append(_list+[c]) # df[5] = [3]+[1,1] or [3]+[3]

    return dp[target]


candidates = [2,3,6,7]
'''0    1   2   3    4     5      6    |    7
2 [ ]  [ ] [2]  x  [2,2]   x   [2,2,2] |    x
3 [ ]  [ ] [ ] [3]   x   [3,2] [3,3]   | [3,2,2]
6 [ ]  [ ] [ ] [ ]  [ ]   [ ]    [6]   |    x
7 [ ]  [ ] [ ] [ ]  [ ]   [ ]    [ ]   | [7]
'''
target = 7
expected = [
  [2,2,3],
  [7]
]       
actual = combination_sum(candidates, target)
print(expected == actual)