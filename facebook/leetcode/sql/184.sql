"""184. Department Highest Salary
https://leetcode.com/problems/department-highest-salary/

Write a SQL query to find employees who have the highest salary in each of the departments. 
For the above tables, your SQL query should return the following rows (order of rows does not matter).

Employee Table:
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+

Department Table:
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+

Results Table:
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
"""
SELECT 
    d.name AS Department, 
    e.name AS Employee, 
    Salary 
FROM Employee e 
JOIN Department d on e.DepartmentId = d.Id 
-- need a DepartmentId here because if a max salary is found in two departments
-- it will return the employee from a different department that matches the salary
WHERE (e.DepartmentId, Salary) IN (
    SELECT 
        DepartmentId,
        MAX(salary)  
    FROM Employee
    GROUP BY DepartmentId
);
