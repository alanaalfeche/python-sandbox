"""
Given: Two DNA strings of equal length
Retrun: Hamming distance or the minimum substitution required to transform to one another
"""

seq1 = "GAGCCTACTAACGGGAT"
seq2 = "CATCGTAATGACGGCCT"

mismatch = 0
for i in range(len(seq1) - 1):
    if seq1[i] != seq2[i]:
        mismatch += 1

print(mismatch)