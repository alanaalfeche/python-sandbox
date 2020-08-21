'''Problem 208: Implement Trie (Prefix Tree)

https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with insert, search, and startsWith methods.
'''


class Trie:


    def __init__(self):
        self.trie = {}


    def insert(self, word: str) -> None:
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'


    def search(self, word: str) -> bool:
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
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