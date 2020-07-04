"""Problem 13: Roman to Integer
https://leetcode.com/problems/roman-to-integer/

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
"""
def solution(roman_numeral: str) -> int:
    """Returns integer equivalent of a roman numeral from a roman to int map. 
    Subtracts previous integer if current roman is greater than previous roman.
    Otherwise, it simply adds to the total integer value. 

    Time Complexity: n
    Space Complexity: constant
    Runtime: 32 ms, faster than 98.81% of Python3 online submissions for Roman to Integer.
    Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Roman to Integer.
    """
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    prev = None
    roman_to_int = 0
    for char in roman_numeral:
        if prev is None:
            prev = char
        elif roman_map[prev] < roman_map[char]:
            roman_to_int += roman_map[char] - roman_map[prev]
            prev = None
        else:
            roman_to_int += roman_map[prev]
            prev = char

    if prev is not None:
        roman_to_int += roman_map[prev]

    return roman_to_int

print(solution('XIV'))