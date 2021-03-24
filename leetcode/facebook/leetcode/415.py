"""415. Add String
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
    p1 = len(num1) - 1
    p2 = len(num2) - 1
    while p1 >= 0 or p2 >= 0:
        x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
        x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0

        value = (x1 + x2 + carry) % 10
        carry = (x1 + x2 + carry) // 10

        res.append(value)
        p1 -= 1
        p2 -= 1

    if carry:
        res.append(carry)

    return ''.join(str(x) for x in res[::-1])

expected = "108"
actual = addStrings("9", "99")
print(actual == expected)