from typing import List

"""953. Verifying an Alien Dictionary
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, 
return true if and only if the given words are sorted lexicographicaly in this alien language.
"""
def isAlienSorted(words: List[str], order: str) -> bool:
    o_idx = {c: idx for idx, c in enumerate(order)}

    for i in range(len(words)-1):
        a = words[i]
        b = words[i+1]

        for j in range(min(len(a), len(b))):
            if a[j] != b[j]:
                if o_idx[a[j]] > o_idx[b[j]]: 
                    return False
                break
        else:
            if len(a) > len(b): return False
    
    return True


words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
expected = False
actual = isAlienSorted(words,  order)
print(expected == actual)