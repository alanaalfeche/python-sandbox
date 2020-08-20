'''Problem 73: Set Matrix Zeroes

https://leetcode.com/problems/set-matrix-zeroes/

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
'''

def set_zeroes(matrix):
    '''This algorithm uses set() to track the row and column indices at which 0 is found. This is to ensure there is no redundancy when we set these indices to 0.

    Once we have the list of row and column indices:
    For rows, we iterate from 0 -> n (number of columns) and set M[r][n] = 0 --> horizontal zeroing
    For columns, we iterate from 0 -> m (number of rows) and set M[m][c] = 0 --> vertical zeroing

    This is an n^2 solution.
    '''
    m = len(matrix)
    n = len(matrix[0])
    
    r_zeroes = set()
    c_zeroes = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                r_zeroes.add(i)
                c_zeroes.add(j)

    for r in r_zeroes:
        for j in range(n):
            matrix[r][j] = 0

    for c in c_zeroes:
        for i in range(m):
            matrix[i][c] = 0

    return matrix


matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
expected = [
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
actual = set_zeroes(matrix)
print(actual == expected)