'''
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
'''

def min_windows(s, t):
    size = len(t)
    t_dict = {c:1 for c in list(t)}

    result = s
    x = 0
    m = 2
    for i, c in enumerate(s):
        if c in t_dict.keys():
            t_dict[c] += 1
        if sum(t_dict.values()) == m * size:
            temp = s[x:i+1]
            print(temp)
            if len(result) > len(temp):
                result = temp
            x = i
            m += 1
        
    return result


s = "ADOBECODEBANC"
t = "ABC"
expected = "BANC"
actual = min_windows(s, t)
print(actual == expected)