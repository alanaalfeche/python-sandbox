"""415. Add String
https://leetcode.com/problems/add-strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
    1. The length of both num1 and num2 is < 5100.
    2. Both num1 and num2 contains only digits 0-9.
    3. Both num1 and num2 does not contain any leading zero.
    4. You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
def addStrings(num1: str, num2: str) -> str:
    res = []
    carry = 0
    x0 = ord('0')

    n1 = len(num1) - 1
    n2 = len(num2) - 1
    while n1 >= 0 or n2 >= 0:
        x1 = ord(num1[n1]) - x0 if n1 >= 0 else 0
        x2 = ord(num2[n2]) - x0 if n2 >= 0 else 0

        sum = (x1 + x2 + carry) % 10 
        carry = (x1 + x2 + carry) // 10

        res.append(sum)

        n1 -= 1
        n2 -= 1
    
    if carry:
        res.append(carry)

    return ''.join(str(x) for x in res[::-1])

assert addStrings("99", "9") == "108"
