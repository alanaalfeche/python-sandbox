# Authored By: Ben L. and Jacob P. from Coursera
# Modified By: Alana Alfeche

def naive(pattern, text):
    occurences = []
    for i in range(len(text) - len(pattern)):
        match = True
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                match = False
                break
        if match:
            occurences.append(i+1)
    print(" ".join(map(str, occurences)))

naive('ATAT', 'GATATATGCATATACTT')