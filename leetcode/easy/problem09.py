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

def isPalindrome(num: int) -> bool:
    """
    Runtime: 56 ms, faster than 84.96% of Python3 online submissions for Palindrome Number.
    Memory Usage: 13.7 MB, less than 85.66% of Python3 online submissions for Palindrome Number.
    """
    orig = num
    if num < 0 or (num % 10 == 0 and num != 0):
        """
        Edge Case #1: number is negative e.g. -12 -> 21- --> Not palindrome
        Edge Case #2: multiple of 0 e.g. 30 -> 03 --> Not palindrome
        """
        return False
    
    rev = 0
    while num > 0:
        rev = (10*rev) + num % 10
        num //= 10

    return rev == orig

print(isPalindrome(313))
