"""
Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file.
        Assume 1-based numbering of lines.
"""
counter = 1
with open('python_village/INI5_input') as f:
    for line in f: 
        line = line.rstrip()
        if counter % 2 == 0:
            print(line)
        counter = counter + 1
