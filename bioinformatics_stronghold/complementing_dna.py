dna = "AAAACCCGGT"
complement = ""

for char in dna:
    new_char = ""

    if char == "A":
        new_char = "T"
    elif char == "T":
        new_char = "A"
    elif char == "C":
        new_char = "G"
    elif char == "G":
        new_char = "C"

    complement = new_char + complement

print(complement)