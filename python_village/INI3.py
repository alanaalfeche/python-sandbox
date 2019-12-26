"""
Given: A string s of length at most 200 letters and four integers a, b, c and d.
Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. 
In other words, we should include elements s[b] and s[d] in our slice.
"""
string = input("Provide a string to splice: ")
splice_sites = input("Provide splice sites: ")
ss_list = list(map(int, splice_sites.split()))
print(ss_list)

for splice_site in range(0, len(ss_list)-1, 2):
    ss_pair = ss_list[splice_site:splice_site+2]
    word = string[ss_pair[0]:ss_pair[1]+1] # inclusive
    print(word)
