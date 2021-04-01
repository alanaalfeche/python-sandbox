"""176. Second Highest Salary
https://leetcode.com/problems/second-highest-salary/submissions/

Write a SQL query to get the second highest salary from the Employee table.
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
"""
-- By encapsulating the query with outer select, 
-- the query returns NULL value if inner select returns 0 matching rows
SELECT(
    SELECT DISTINCT Salary -- We also added a distinct for cases where salary occurs more than once
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;

-- Alternative approach:
SELECT IFNULL(
    (
        SELECT salary
        FROM Employee
        GROUP BY salary
        ORDER BY salary DESC
        LIMIT 1 OFFSET 1
    ), NULL
) as SecondHighestSalary