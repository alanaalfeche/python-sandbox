'''Problem 76: Minimum Window Substring

https://leetcode.com/problems/minimum-window-substring/

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
'''
from collections import Counter


def min_windows(s, t):
    '''This algorithm uses sliding window to find the minimum substring in which all characters in T is satisfied. 

    It starts by creating a hashmap for string T and initializing a missing variable to store the number of missing characters. 

    Starting at index 0, we let r traverse through the list, checking if current char is found in the hashmap and decrementing missing if it is found. 

    When we find all the missing character, we go inside the nested while loop to move l as close to r without incrementing missing. 

    We also set the best start and end indices inside this while loop which we ultimately return as the minimum substring.
    '''
    need = Counter(t)
    missing = len(t)

    l, r, i, j = 0, 0, 0, 0
    while r < len(s):
        if need[s[r]] > 0: # subtract if char in s satisfy a char in t
            missing -= 1
        need[s[r]] -= 1
        r += 1

        while missing == 0: # contract l until we find start missing a char in t
            if j == 0 or r - l < j - i: 
                i, j = l, r
            need[s[l]] += 1
            if need[s[l]] > 0: # if char in t is found then break out from the while loop
                missing += 1
            l += 1 # contract l until a missing char is found

    return s[i:j]


s = "ADOBECODEBANC"
t = "ABC"
expected = "BANC"
actual = min_windows(s, t)
print(actual == expected)