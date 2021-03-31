from typing import List

"""884. Uncommon Words from Two Sentences
https://leetcode.com/problems/uncommon-words-from-two-sentences/

We are given two sentences A and B. (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.
"""
def uncommonFromSentences(A: str, B: str) -> List[str]:
    uncommon = {}

    for a_word in A.split(" "):
        uncommon[a_word] = uncommon.get(a_word, 0) + 1
    
    for b_word in B.split(" "):
        uncommon[b_word] = uncommon.get(b_word, 0) + 1

    return [word for word in uncommon if uncommon[word] == 1]


assert uncommonFromSentences(A="this apple is sweet", B="this apple is sour") == ["sweet","sour"]