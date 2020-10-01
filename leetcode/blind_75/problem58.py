'''Problem 58. Length of Last Word

https://leetcode.com/problems/length-of-last-word/

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.
'''

def length_of_last_word(s):
    fragments = s.split()
    return len(fragments[-1]) if fragments else 0


s = "Hello World"
expected = 5
actual = length_of_last_word(s)
print(expected == actual)