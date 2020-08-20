'''Problem 2: Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.
'''


def length_of_longest_substring(text):
    '''This is a sliding window problem. We start with creating a hashmap which will store char - index as key - value pair, respecitly. 
    
    The start variable determines the index at which no substring has repeating characters whereas the i variable will traverse through the list, expanding the window. 
    
    If a char at index i is found in the hash map then we update the start index to the current index i + 1 (0-based index). 

    Otherwise, we compare the current max length to current index - start index + 1 (0-based index).

    The `and visited[char] >= start` case is added here because we do not want to go back to an earlier starting point if start index is less than current index. 
    '''
    visited = {}
    max_length = start = 0
    for i, char in enumerate(s):
        if char in visited and visited[char] >= start:
            start = visited[char] + 1
        else:
            max_length = max(max_length, i - start + 1)
        visited[char] = i
    return max_length


text = 'tmmzuxt'
expected = 5
actual = solution(text)
print(expected == actual)
