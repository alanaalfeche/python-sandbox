# n = number of months
# k = number of k-rabbit pairs each month
memo = {} 
def fibonacci_rabbit(n, k):
    if (n, k) in memo:
        return memo[(n,k)]
        
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_rabbit(n-1, k) + k*fibonacci_rabbit(n-2, k)

print(fibonacci_rabbit(35, 3))