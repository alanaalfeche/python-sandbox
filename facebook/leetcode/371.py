"""371. Sum of Two Integers

Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""

def getSum(a: int, b: int) -> int:
    """ Why mask?
    Need mask because Python no longer use 8-bit numbers, but INFINITE number of bits
    Useful for non-negative number, but a negative number will have INFINITE number of bits
    Line 12 creates a 32 bit mask of 1's: x & 1 = x
    """
    mask = 0xffffffff 
    while(b & mask > 0):
        a, b = a ^ b, (a & b) << 1

    # if b > 0, the carry bit is "finished". 
    # if not, it will continue until it exceeds the 32 bit mask to end while loop
    return (a & mask) if b > 0 else a


expected = 3
actual = getSum(a=1, b=2)
print(actual == expected)