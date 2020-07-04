"""Blind Curated 75 - Problem 2: Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.
"""
def solution(text: str) -> int:
    """Returns the maximum substring length without repeating character.
    First, it iterates through the char of a string, adding the char - index pair to a hash map. 
    If char is found, and the index of the current char is greater than or equal to the start index, then we update the start index to the current char index + 1. 
    This is used to determine the start window where no repeating character has been found in a substring. 
    Otherwise, return the max of tne current length of substring or the current index minus the start index + 1 because it is 0 based for loop.

    Time Complexity: n
    Space Complexity: min(m, n) where n is the size of string and m is the size of charset/alphabet 
    Runtime: 92 ms, faster than 29.29% of Python3 online submissions for Longest Substring Without Repeating Characters.
    Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.
    """
    char_map = {}
    start = 0
    len_string = 0

    for i, char in enumerate(text):
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        else:
            len_string = max(len_string, i - start + 1)
        
        char_map[char] = i
        
    return len_string

print(solution("tmmzuxt"))
