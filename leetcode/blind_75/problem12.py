'''
Problem 49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Given an array of strings, group anagrams together.
'''


def group_anagram(strs):
    strs_sorted = []
    for s in strs:
        strs_sorted.append(''.join(sorted(s)))

    anagrams = {}
    for index, s in enumerate(strs_sorted):
        if s not in anagrams:
            anagrams[s] = [index]
        else:
            anagrams[s].append(index)

    result = []
    for group in anagrams.values():
        sub_group = []
        for value in group:
            sub_group.append(strs[value])
        result.append(sub_group)

    return result


strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
expected = [
    ["eat","tea","ate"],
    ["tan","nat"],
    ["bat"]
]

actual = group_anagram(strings)
print(actual == expected)