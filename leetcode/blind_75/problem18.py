'''Problem 18: Unique Paths

https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''
def unique_paths(m, n):
    '''This algorithm is built on the findings that unique path for each item M[i][j] in the matrix is simply the sum of M[i-1][j] + M[i][j-1]
        0   1   2   
    0   1   1   1
    1   1   1   1

        0   1   2   
    0   1   1   1
    1   1   2   3 = M[1][2] + M[2][1]
    '''
    M = [[1] * m for _ in range(n)]
    print(M)
    for i in range(1, n): # skipping first row 
        for j in range(1, m): # skipping first column
            M[i][j] = M[i-1][j] + M[i][j-1]
    
    return M[-1][m-1]


m = 3
n = 2
expected = 3
actual = unique_paths(m, n)
print(expected == actual)

