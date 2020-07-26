'''
Problem 3: Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''
def brute_force_solution(text: str) -> str:
    sub_text = ''
    for i in range(len(text)):
        for j in range(len(text), i, -1):
            if j-i <= len(sub_text): # do not bother for text less than the current substring
                break
            elif text[i:j] == text[i:j][::-1]: 
                sub_text = text[i:j]
    return sub_text
    
print(brute_force_solution("babad"))
