"""Problem 9: Palindrome Number
https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
"""
def crooked_isPalindrome(num: int) -> bool:
    """Returns False for all negative input numbers.
    Compare the stringified reversed integer to original integer for non-negative input numbers.
    Crooked because we are not allowed to convert it to string for this problem.

    Time Complexity: math
    Space Complexity: non-constant for creating the string
    Runtime: 60 ms, faster than 64.38% of Python3 online submissions for Palindrome Number.
    Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Palindrome Number.
    """
    return False if num < 0 else num == int(str(num)[::-1])

print(crooked_isPalindrome(313))