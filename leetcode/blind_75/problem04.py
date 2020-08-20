'''Problem 4: Container With Most Water

https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 

Find two lines, which together with x-axis forms a container, such that the container contains the most water.
'''


def max_area(alist) -> int:
    if len(alist) < 2:
        return 
    
    i, j = 0, len(alist) - 1
    area = 0
    while i < j: 
        area = max(area, min(alist[j], alist[i]) * (j - i))
        if alist[i] < alist[j]: i += 1
        else: j -= 1
            
    return area


height = [1,8,6,2,5,4,8,3,7]
expected = 49
actual = max_area(height)
print(expected == actual)
