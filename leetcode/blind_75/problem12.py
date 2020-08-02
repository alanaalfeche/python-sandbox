'''
Problem 49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Given an array of strings, group anagrams together.

Solution authored by NDW: https://github.com/nolanwrightdev/blind-75-python/blob/master/problems/problem13.py
'''


def group_anagram(strs):
	anagrams = {}
	for s in strs:
		characters = [0] * 26
		for char in s:
			characters[ord(char) - ord('a')] += 1
		tup = tuple(characters)
		'''
		Why do we have to convert characters type list to type tuple?

		The builtin list type should not be used as a dictionary key.
		Note that since tuples are immutable, they do not run into the troubles of lists - they can be hashed by their contents without worries about modification. 
		Thus, in Python, they provide a valid __hash__ method, and are thus usable as dictionary keys.

		https://wiki.python.org/moin/DictionaryKeys		
		'''
		anagrams[tup] = anagrams.get(tup, []) + [s]
	return anagrams.values()


strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagram(strings))
