"""
Problem 208 - Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with insert, search, and startsWith methods.
"""


class Trie:


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True


trie = Trie()
trie.insert('alana')
trie.insert('joy')
trie.insert('ballesteros')
trie.insert('alfeche')
# print(trie.search('alana'))     # True
# print(trie.search('always'))    # False
# print(trie.startsWith('al'))    # True
# print(trie.startsWith('joy'))   # True
# print(trie.startsWith('ball'))  # True