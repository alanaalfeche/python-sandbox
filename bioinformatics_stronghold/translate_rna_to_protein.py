"""
Given: An RNA string
Return: Protein!
"""

rna_codon_table = { "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
                    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
                    "UAU":"Y", "UAC":"Y", "UAA":"", "UAG":"",
                    "UGU":"C", "UGC":"C", "UGA":"", "UGG":"W",
                    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
                    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
                    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
                    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
                    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
                    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G", }

counter = 0
protein = ""
with open('bioinformatics_stronghold/sample_rna') as f:
    temp = ""
    for line in f:
        for char in line:
            temp += char

            if len(temp) == 3:
                protein = protein + rna_codon_table[temp]
                temp = ""

print(protein)