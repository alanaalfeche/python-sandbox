"""
Given: At most 10 DNA strings in FASTA format
Result: The ID of the string having the highest GC-content, followed by the GC-content
"""
max_gc_id = ""
max_gc_count = 0

def gc_content_counter(filename):
    gc_id = ""
    gc_count = 0
    seq_length = 0
    
    counter = 0
    with open(filename, 'r') as f:
        for line in f:
            if line[0] is '>':
                if counter == 0:
                    gc_id = line.split('>')[1] 
                else:
                    gc_content_compare(gc_id, gc_count, seq_length)
                    gc_id = line.split('>')[1]
                    gc_count = seq_length = 0
                counter += 1
            elif line[0] is not '>':
                for char in line.rstrip():                    
                    if char == 'G' or char == 'C':
                        gc_count += 1
                    seq_length += 1

    gc_content_compare(gc_id, gc_count, seq_length)

def gc_content_compare(gc_id, gc_count, seq_length):
    gc_content = gc_count / seq_length

    global max_gc_count, max_gc_id
    if gc_content > max_gc_count:
        max_gc_id = gc_id
        max_gc_count = gc_content

gc_content_counter('bioinformatics_stronghold/gc_content')
print(max_gc_id, max_gc_count * 100)
