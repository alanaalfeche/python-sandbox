from typing import List
"""
Problem 4 - Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
"""
def time_limited_solution(height: List[int]) -> int:
    """Only suitable for low quantity of values in list
    
    Time Complexity: n^2
    Space Complexity: constant
    """
    area = 0
    for i in range(0, len(height)-1):
        for j in range(i+1, len(height)):
            area = max(area, min(height[i], height[j]) * (j-i))
    return area    

print(time_limited_solution([1,8,6,2,5,4,8,3,7]))

def optimized_solution(alist: List[int]) -> int:
    """Optimized first solution to prevent calculate all possible areas by limiting scope

    Runtime: 132 ms, faster than 76.23% of Python3 online submissions for Container With Most Water.
    Memory Usage: 15.4 MB, less than 34.56% of Python3 online submissions for Container With Most Water.
    """
    if len(alist) < 2:
        return 
    
    low, high = 0, len(alist) - 1
    area = 0
    
    while low < high: 
        area = max(area, min(alist[high], alist[low]) * (high - low))
        if alist[low] < alist[high]: low += 1
        else: high -= 1
            
    return area

print(optimized_solution([1,8,6,2,5,4,8,3,7]))
