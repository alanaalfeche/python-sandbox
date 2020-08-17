'''
Problem 125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''


def is_palindrome(s) -> bool:
    text = ''.join([i.lower() for i in s if (i.isalpha() or i.isnumeric())])
    return text == text[::-1]


s = "A man, a plan, a canal: Panama"
expected = True
actual = is_palindrome(s)
print(expected == actual)