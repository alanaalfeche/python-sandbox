def consensus_generator(consensus_string):
    consensus = ""

    for j in range(len(consensus_string[0])):
        temp_max = 0
        temp_max_index = 0

        for i in range(4):
            if consensus_string[i][j] > temp_max:
                temp_max = consensus_string[i][j]
                temp_max_index = i
        
        if temp_max_index == 0:
            consensus += 'A'
        elif temp_max_index == 1:
            consensus += 'C'
        elif temp_max_index == 2:
            consensus += 'G'
        elif temp_max_index == 3:
            consensus += 'T'

    print(consensus)
    printer(consensus_string)

def profile_generator(dna_strings):
    # initializing 2D array of sequences profile
    consensus_string = [[0 for x in range(len(dna_strings) + 1)] for y in range(4)]

    for row, sequence in enumerate(dna_strings):
        for column, char in enumerate(sequence):
            if char == 'A':
                consensus_string[0][column] += 1
            elif char == 'C':
                consensus_string[1][column] += 1
            elif char == 'G':
                consensus_string[2][column] += 1
            elif char == 'T':
                consensus_string[3][column] += 1
    
    # printer(consensus_string)
    consensus_generator(consensus_string)

def dna_strings_generator(sequences):
    # initializing 2D array of sequences
    dna_strings = [[0 for x in range(len(sequences[0]))] for y in range(len(sequences))]

    for row, sequence in enumerate(sequences):
        for column, char in enumerate(sequence):
            dna_strings[row][column] = char

    # printer(dna_strings)
    profile_generator(dna_strings)

def main(filename):
    sequences=[]
    with open(filename, 'r') as f:
        for line in f:
            if line[0] is not '>':
                sequences.append(line.rstrip())

    dna_strings_generator(sequences)

def printer(sequences):
    for row in sequences:
        print(str(row))

if __name__ == "__main__":
    main('bioinformatics_stronghold/consensus_string_sample')
