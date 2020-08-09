'''
Problem 48. Rotate Image
https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise) and in-place.
'''


def rotate(matrix):
    n = len(matrix)
    matrix.reverse() # can also use matrix[::-1]
    '''
    The transpose of matrix A is commonly denoted as A^t 
    A transpose of matrix is an operator which flips a matrix over its diagonal

    1. Reflect A over its main diagonal (top-left to bottom-right)
    2. Write the rows of A as the columns of A^t 
    3. Write the columbs of A as the rows of A^t
    
    e.g 
        A = [1][2]      A^t = [1]
                              [2]

        A = [1][2]      A^t = [1][3]
            [3][4]            [2][4]  

        A = [1][2]      A^t = [1][3][5]
            [3][4]            [2][4][6] 
            [5][6]

        A = [1][2][3]      A^t = [1][4][7]
            [4][5][6]            [2][5][6] 
            [7][8][9]            [3][8][9]

    Reverse + Transpose rotate a matrix in 90 degrees

    A_r = [7][8][9]      (A_r)^t = [7][4][1]
          [4][5][6]                [8][5][2] 
          [1][2][3]                [9][6][3]

    More fun solutions: https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)
    '''
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

expected = [
    [7,4,1],
    [8,5,2],
    [9,6,3]
]

actual = rotate(matrix)
print(actual == expected)