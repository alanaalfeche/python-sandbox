"""Problem 7 - Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
"""

def isValid(text: str) -> bool:
    """
    Stack follows a LIFO - last in and first out pattern. 
    We first traverse through the set of characters in a text. 
    When an opening bracket is found, it is added to the stack.
    When a closing bracket is found, the mapping is used to see if the last added character matches the accompanying pair of the closing bracket. If not, it returns False.

    Runtime: 28 ms, faster than 72.45% of Python3 online submissions for Valid Parentheses.
    Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
    Time Complexity: O(n)
    Space Complexity: O(n) for stack
    """
    mapping = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    
    stack = []
    
    for char in text:
        if char in mapping: # add closing BRACKETS
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        
        else: # add opening brackets
            stack.append(char)
            
    # an empty stack returns False
    # so we return the opposite of bool
    return not bool(stack)

print(isValid('([{}])'))
print(isValid('()[]{}'))

