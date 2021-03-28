"""67. Add Binary

Given two binary strings a and b, return their sum as a binary string.
"""
def addBinaryWithBuiltInFunctions(a: str, b: str) -> str:
    return '{0:b'.format(int(a, 2) + int(b, 2))


def bitByBitComputation(a: str, b: str) -> str:
    n = max(len(a), len(b))
    # add zeroes at the beginning of string
    # until it reaches the specified length
    a, b = a.zfill(n), b.zfill(n)

    carry = 0
    answer = []
    for i in range(n-1, -1, -1):
        if a[i] == "1":
            carry += 1
        if b[i] == "1":
            carry += 1

        if carry % 2 == 1:
            answer.append('1')
        else:
            answer.append('0')

        carry = carry // 2

    if carry == 1:
        answer.append('1')
    answer.reverse()

    return ''.join(answer)

""" Bitwise XOR
Bitwise XOR or "exclusive OR" can return the sum of two binary integer: sum =  x ^ y 
This is because XOR lets you flip the bits using a mask in a reversable operation

a | b | a ^ b
--|---|------
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 0
"""

""" Bitwise AND
Bitwise AND can return the carry of two binary integer: carry =  x & y 

a | b | a & b
--|---|------
0 | 0 | 0
0 | 1 | 0
1 | 0 | 0
1 | 1 | 1
"""
def bitManipulation(a: str, b: str) -> str:
    x, y = int(a, 2), int(b, 2)
    while y:
        answer = x ^ y
        carry = (x & y) << 1
        x, y = answer, carry
        # reduced version: x, y = x ^ y, (x & y) << 1
    return bin(x)[2:]

def addBinary(a: str, b: str) -> str:
    res = ""
    carry = False

    n = max(len(a), len(b))
    a, b = a.zfill(n), b.zfill(n)
    
    for a, b in zip(reversed(a), reversed(b)):
        count = 0
        if a == "1": 
            count += 1
        if b == "1":
            count += 1
        if carry:
            count += 1

        if count == 0:
            res += '0'
            carry = False
        elif count == 1:
            res += "1"
            carry = False
        elif count == 2:
            res += '0'
            carry = True
        elif count == 3:
            res += "1"
            carry = True

    if carry:
        res += "1"

    return res[::-1]

expected = "100"
actual = addBinary(a="11", b="1")
print(actual)
print(expected == actual)