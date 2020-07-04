sample_seq = "AAAACCCGGT"
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
reverse_complement = ""

for base in sample_seq:
    base_complement = complement[base]
    reverse_complement = base_complement + reverse_complement

print(reverse_complement)