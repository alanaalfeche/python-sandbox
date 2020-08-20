'''Problem 70: Climbing Stairs

https://leetcode.com/problems/climbing-stairs/

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


cache = {}
def climb_stairs(n):
    '''This is similar to fibonacci problem where each unique ways to climb a step n is dependent on the unique ways to climb (n-2) + (n-1).
    
    This uses recursion with memoization to remove redundancy that we see often with regular fibonacci-recursion problems.
    '''
    if n in cache:
        return cache[n]

    if n <= 1:
        result = 1
    elif n == 2:
        result = 2
    else:
        result = climb_stairs(n-2) + climb_stairs(n-1)

    cache[n] = result
    return result


n = 3
expected = 3
actual = climb_stairs(n)
print(actual == expected)
