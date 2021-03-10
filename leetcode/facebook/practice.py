"""
Write a function that returns the elements on odd positions (0 based) in a list
"""
def solution(input):
    return [i for idx, i in enumerate(input) if idx % 2 != 0]

assert solution([0,1,2,3,4,5]) == [1,3,5] 
assert solution([1,-1,2,-2]) == [-1,-2]


"""
Write a function that returns the cumulative sum of elements in a list
"""
def solution2(input):
    for idx in range(1, len(input)):
        input[idx] = input[idx-1] + input[idx]
    return input

assert solution2([1,1,1]) == [1,2,3]
assert solution2([1,-1,3]) == [1,0,3]


"""
Write a function that takes a number and returns a list of its digits
"""
def solution3(input):
    return [int(i) for i in str(input)]

assert solution3(123) == [1,2,3] 
assert solution3(400) == [4,0,0]


"""
From: http://codingbat.com/prob/p126968
Return the "centered" average of an array of ints, which we'll say is
the mean average of the values, except ignoring the largest and smallest values in the array. 
If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. 
Use int division to produce the final average. 
You may assume that the array is length 3 or more.
"""
def solution4(input): 
    return (sum(input) - min(input) - max(input)) // (len(input) - 2)


assert solution4([1, 2, 3, 4, 100]) == 3
assert solution4([1, 1, 5, 5, 10, 8, 7]) == 5 
assert solution4([-10, -4, -2, -4, -2, 0]) == -3