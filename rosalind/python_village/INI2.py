"""
Given: Two positive integers a and b, each less than 1000.
Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.
"""
a=975
b=812

if (a and b < 1000):
    print(a**2 + b**2)