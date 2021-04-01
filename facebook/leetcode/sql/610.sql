"""610. Triangle Judgement
https://leetcode.com/problems/triangle-judgement/

Write a query to judge whether these three sides can form a triangle
| x  | y  | z  |
|----|----|----|
| 13 | 15 | 30 |
| 10 | 20 | 15 |

For the sample data above, your query should return the follow result:
| x  | y  | z  | triangle |
|----|----|----|----------|
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
"""
-- A triangle can form if the sum of any of two segments is larger than the third one
-- Approach 1: Use CASE WHEN 
SELECT 
    x, 
    y, 
    z,
    CASE
        WHEN x + y > z and x + z > y AND y + z > x THEN "Yes"
        ELSE "No"
    END AS "triangle"
FROM triangle;

-- Approach 2: IF statement
SELECT 
    x, 
    y,
    z,
    IF (x + y > z and x + z > y AND y + z > x, "Yes", "No") as "triangle"
FROM triangle;