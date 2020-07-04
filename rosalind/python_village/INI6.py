"""
Given: A string s of length at most 10000 letters.
Return: The number of occurence of each word in s, where words are separated by spaces. 
Words are case-sensitive and the lines in output can be in any order.
"""

sample_text="We tried list and we tried dicts also we tried Zen"
text_count={}

split_text = sample_text.split()

for text in split_text:
    if text in text_count:
        text_count[text] += 1
    else:
        text_count[text] = 1

for result in text_count:
    print(result, text_count[result])
