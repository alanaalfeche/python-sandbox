"""Blind Curated 75 - Problem 3: Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""
def brute_force_solution(text: str) -> str:
    """Pick all starting and ending positions for a substring and verify that it is a palindrome.

    Time Complexity: n^3 - An n string have n/2*(n-1) substrings, then there's the added n to verify each substring 
    Space Complexity: constant
    Runtime: 4980 ms, faster than 21.58% of Python3 online submissions for Longest Palindromic Substring.
    Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Longest Palindromic Substring.
    """
    sub_text = ''
    for i in range(len(text)):
        for j in range(len(text), i, -1):
            if j-i <= len(sub_text): # do not bother for text less than the current substring
                break
            elif text[i:j] == text[i:j][::-1]: 
                sub_text = text[i:j]
    return sub_text
    
print(brute_force_solution("babad"))