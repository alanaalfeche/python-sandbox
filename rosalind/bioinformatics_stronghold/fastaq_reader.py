def read_fastq(filename):
    sequences = []
    qualities = []

    with open(filename) as f:
        while True:
            f.readline()
            seq = f.readline().rstrip()
            f.readline()
            qual = f.readline().rstrip()

            if len(seq) == 0:
                break
        
            sequences.append(seq)
            qualities.append(qual)

    print(sequences, qualities)

read_fastq("bioinformatics_stronghold/fastaq_sample")
