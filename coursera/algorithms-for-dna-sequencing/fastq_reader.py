def read_fastq(file_path):
    sequences = []
    qualities = []

    with open(file_path, 'r') as f:
        while True:
            f.readline()
            sequence = f.readline().rstrip()
            f.readline()
            quality = f.readline().rstrip()

            if len(sequence) == 0:
                break

            sequences.append(sequence)
            qualities.append(quality)

    return sequences, qualities
    
read_fastq('algorithms-for-dna-sequencing/sample.fastq')