'''
Problem 18. Unique Paths
https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''
def unique_paths(m, n):
    M = [[1] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            M[i][j] = M[i-1][j] + M[i][j-1]
    
    return M[-1][m-1]


m = 3
n = 2
expected = 3
actual = unique_paths(m, n)
print(expected == actual)

