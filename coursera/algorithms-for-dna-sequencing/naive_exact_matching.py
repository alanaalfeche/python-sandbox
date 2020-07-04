def read_sequence(filename):
    sequence = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                sequence += line.rstrip()

    return sequence

def reverse_complement(sequence):
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

    reversed_string = ""
    for base in sequence:
        reversed_string = complement[base] + reversed_string
    
    return reversed_string

def naive_matching(pattern, text, max_mismatch=0):
    occurences = []

    for i in range(len(text) - len(pattern) + 1):

        mismatch = 0
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                mismatch += 1

        if mismatch <= max_mismatch:
            occurences.append(i)

    return occurences

def main(pattern, file_name, max_mismatch):
    text = read_sequence(file_name)
    reverse_pattern = reverse_complement(pattern)

    result = naive_matching(pattern, text, max_mismatch)

    if pattern != reverse_pattern:
        result.extend(naive_matching(reverse_pattern, text))

    result.sort()

    print(len(result))
    print(result)

if __name__ == "__main__":
    pattern = "AGGAGGTT"
    file_name = "algorithms-for-dna-sequencing/lambda_virus_sample.fa"
    max_mismatch = 2

    main(pattern, file_name, max_mismatch)

