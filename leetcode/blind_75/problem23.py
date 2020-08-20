'''Problem 91: Decode Ways

https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z is being encoded to numbers using the following mapping:
'''


def num_decodings(s):
    '''The answer to any s is the collection of each individual element in s, 
    starting from index zero the index len(s).
    '''
    if not s:
        return 0

    cache = [0 for x in range(len(s) + 1)]
    
    cache[0] = 1
    cache[1] = 0 if s[0] == '0' else 1

    for i in range(2, len(s) + 1):
        if 0 < int(s[i-1]) <= 9:
            cache[i] += cache[i-1]
        if 10 <= int(s[i-2:i]) <= 26:   
            cache[i] += cache[i-2]
    
    return cache[len(s)]


s = '226'
expected = 3 # 226: (2, 2, 6)   (2, 26)    (22, 6)
actual = num_decodings(s)
print(expected == actual)