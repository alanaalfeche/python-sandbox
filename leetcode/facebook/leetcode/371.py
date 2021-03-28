"""371. Sum of Two Integers

Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""

def getSum(a: int, b: int) -> int:
    mask = 0xffffffff
    while(b & mask > 0):
        a, b = a ^ b, (a & b) << 1
    return (a & mask) if b > 0 else a


expected = 3
actual = getSum(a=1, b=2)
print(actual == expected)