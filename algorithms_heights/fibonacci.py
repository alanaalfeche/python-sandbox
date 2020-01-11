'''
Fiboannci numbers forms a fibonacci sequence such that each number F(n) is the sum of the two preceding numbers.
e.g. F(n) = F(n-1) + F(n-2) where F(0) = 0 and F(1) = 1

Fibonacci was introduced to the Western Mathematics by Leonardo of Pisa. 
Though it was first described in Indian Mathematics to study the growth of rabbits population. 
'''

# Fibonacci using recursion
# Time Complexity: O(2^n)
# Space Complexity: maximum depth of the recursion tree ~ n = O(n)
def fibonacci_recursion(num):
    if num <= 1: 
        return num
        
    return fibonacci_recursion(num-1) + fibonacci_recursion(num-2)

print(fibonacci_recursion(6))

# Fibonacci using recursion -- dynamic programming: memoization approach
# Time Complexity: O(n)
# Space Complexity: O(n)
cache = {}
def fibonacci_recursion_with_memoization(num):
    if num in cache:
        return cache[num]

    if num <= 1:
        result = num
    else: 
        result = fibonacci_recursion_with_memoization(num - 2) + fibonacci_recursion_with_memoization(num - 1)

    cache[num] = result
    return result

print(fibonacci_recursion_with_memoization(6))
# Fibonacci using for-loop -- dynammic programming: bottom-up approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def fibonacci_for_loop(num):
    if num <= 1:
        return num

    else:
        a = b = 1
        for _ in range(3, num + 1):
            c = a + b
            a, b = b, c
        return c

print(fibonacci_for_loop(6))