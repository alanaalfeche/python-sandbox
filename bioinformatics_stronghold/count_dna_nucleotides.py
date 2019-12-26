sample_seq = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
seq_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for element in sample_seq:
    if element in seq_count:
        seq_count[element] += 1

for key in seq_count:
    print(seq_count[key])
