"""Problem 7: Reverse Integer 
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.
"""
def reverse(num: int) -> int:
    """
    Time Complexity: constant
    Space Complexity: constant
    Runtime: 24 ms, faster than 93.99% of Python3 online submissions for Reverse Integer.
    Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse Integer.
    """
    if num > 0: # positive input values
        rev_num = int(str(num)[::-1]) 
    else:
        rev_num = -1 * int(str(num*-1)[::-1])

    min = -2**31
    max = 2**31 - 1
    if rev_num not in range(min, max): 
        return 0
    else:
        return rev_num

print(reverse(-12))