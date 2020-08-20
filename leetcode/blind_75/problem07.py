'''Problem 7: Valid Parentheses

https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
'''


def is_valid(text):
    '''We first traverse through the set of characters in a text. When an opening bracket is found, it is added to the stack which has a last in and first out pattern. 

    When a closing bracket is found, the mapping is used to see if the last added character matches the accompanying pair of the closing bracket. If not, it returns False.
    '''
    mapping = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    stack = []
    for char in text:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not bool(stack)


print(is_valid('([{}])'))
print(is_valid('()[]{}'))