dna="GATGGAACTTGACTACGTAAATT"
rna=""

for char in dna: 
    if char == 'T':
        rna += 'U'
    else:
        rna += char

print(rna)