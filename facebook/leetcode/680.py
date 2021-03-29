""" 680. Valid Palindrome II
Given a non-empty string s, you may delete at most one character. 

Judge whether you can make it a palindrome.
"""
def validPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            sleft = s[:left] + s[left+1:]
            sright = s[:right] + s[right+1:]
            return sleft == sleft[::-1] or sright == sright[::-1]
        else:
            left += 1
            right -= 1
    return True 

expected = False
actual = validPalindrome("abc")
assert actual is expected