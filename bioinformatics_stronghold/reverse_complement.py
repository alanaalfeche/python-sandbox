dna = "AAAACCCGGT"
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
reverse_complement = ""

for ntd in dna:
    ntd_complement = complement[ntd]
    reverse_complement = ntd_complement + reverse_complement

print(reverse_complement)