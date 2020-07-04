# Authored By: Ben L. and Jacob P. from Coursera
def naive(pattern, text):
    occurences = []

    for i in range(len(text) - len(pattern) + 1): # 2
        match = True
        for j in range(len(pattern)): # 13
            if text[i+j] != pattern[j]: # 0
                match = False
                break
        if match:
            occurences.append(i)
    
    print(occurences)

naive('AGCT', 'AGCTTAAGCT')