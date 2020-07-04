"""Problem 14: Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
def solution(sample):
    """
    Construct a matrix for each string in the list.
    Then, perform a comparison of character in each row with a given column index.

    Time Complexity: 
    Space Complexity: 
    Runtime: 32 ms, faster than 67.63% of Python3 online submissions for Longest Common Prefix.
    Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.
    """
    # return empty string for an empty list
    if not sample:
        return ''

    # returns the longest string in list using len as the indicator
    col = len(max(sample, key=len)) 
    row = len(sample) 

    # create and build matrix to house the characters of each string
    matrix = [[0] * col for _ in range(row)] 
    for i, item in enumerate(sample):
        for j in range(0, len(item)):
            matrix[i][j] = item[j]
    
    prefix = ''
    # iterating through the row with a specified col index to see if they all match
    for l in range(0, col):   
        char = None
        for k in range(0, row): 
            if char is None:
                char = matrix[k][l]
            elif char != matrix[k][l]:
                char = ''
                break
        
        if l == 0 and len(char) == 0:
            return ''
        else:
            prefix += char
            char = None

    return prefix

print(solution(["flower","flow","flight"])) # fl
