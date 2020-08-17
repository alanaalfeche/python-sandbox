'''
Problem 125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''


def is_palindrome(s) -> bool:
    # Authored By NDW: https://github.com/nolanwrightdev/blind-75-python/blob/master/problems/problem32.py
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


s = "A man, a plan, a canal: Panama"
expected = True
actual = is_palindrome(s)
print(expected == actual)