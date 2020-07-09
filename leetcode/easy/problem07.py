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

def reverse2(num: int) -> int:
    """
    Runtime: 48 ms, faster than 16.29% of Python3 online submissions for Reverse Integer.
    Memory Usage: 13.6 MB, less than 96.37% of Python3 online submissions for Reverse Integer.
    """
    sign = [1, -1][num < 0] # returns [1, -1][0] if position, [1, -1][1] if negative
    rev = sign * int(str(abs(num))[::-1])
    return rev if -(2**31)-1 < rev < 2**31 else 0

def reverse3(num: int) -> int:
    rev = 0
    while num > 0:
        rev = (10*rev) + num % 10
        num //= 10
        # // int
        # /  float
    return rev

print(reverse(-12))
print(reverse2(-123))
print(reverse3(1234))
