"""
Given: Two positive integers a and b (a < b < 1000).
Return: The sum of all odd integers from a through b, inclusively

An integer is off if it is not a multiple of 2.
"""
a=4390
b=8840

total = 0

for num in range(a, b):
    if num % 2 != 0:
        total = total + num

print(total)