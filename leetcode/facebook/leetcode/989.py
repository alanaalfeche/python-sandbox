from typing import List

""" 989. Add to Array-Form of Integer

For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  
For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.
"""

def addToArrayForm(A: List[int], K: int) -> List[int]:
    K = list(map(int, str(K)))
    result = []
    carry = 0

    a = len(A) - 1
    k = len(K) - 1

    while a >= 0 or k >= 0:
        x1 = A[a] if a >= 0 else 0
        x2 = K[k] if k >= 0 else 0

        res = (x1 + x2 + carry) % 10
        carry = (x1 + x2 + carry) // 10
        
        result.append(res)
        
        a -= 1
        k -= 1

    if carry:
        result.append(carry)

    return result[::-1]


expected = [1, 2, 3, 4]
actual = addToArrayForm(A=[1, 2, 0, 0], K=34)
print(expected == actual)
