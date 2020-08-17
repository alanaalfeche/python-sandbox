'''
79. Word Search
https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 

The same letter cell may not be used more than once.
'''
def exist(board, word):
    if not board or not word:
        return False

    stack = list(word)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] in stack:
                stack.remove(board[i][j])
     
    return not bool(stack)


board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = 'ABCCED'
expected = False
actual = exist(board, word)
print(expected == actual)