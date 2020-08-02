'''
Problem 70. Climbing Stairs
https://leetcode.com/problems/group-anagrams/

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
cache = {}
def climb_stairs_memoization(n):
    # dynamic programming - recursion with memoization
    
    if n in cache:
        return cache[n]

    if n <= 1:
        result = 1
    elif n == 2:
        result = 2
    else:
        result = climb_stairs_memoization(n-2) + climb_stairs_memoization(n-1)

    cache[n] = result
    return result

def climb_stairs_bottom_up(n):
    # dynamic programming - bottom-up solution
    if n <= 1:
        return 1
    else:
        a = 1
        b = 2
        for _ in range(3, n + 1):
            c = a + b 
            a, b = b, c
        return c

sample = 3
actual = climb_stairs_memoization(sample)
actual2 = climb_stairs_bottom_up(sample)
print(actual == actual2)
