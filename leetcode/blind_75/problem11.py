'''
Problem 48. Rotate Image
https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise) and in-place.
'''


def rotate(matrix):
    n = len(matrix)
    matrix.reverse() # can also use matrix[::-1]
    for i in range(n):
        for j in range(i + 1, n):
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