"""181. Employees Earning More Than Their Managers
https://leetcode.com/problems/employees-earning-more-than-their-managers/

The Employee table holds all employees including their managers.
Every employee has an Id, and there is also a column for the manager Id.
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+

Given the Employee table, write a SQL query that finds out employees who earn more than their managers.
For the above table, Joe is the only employee who earns more than his manager.
+----------+
| Employee |
+----------+
| Joe      |
+----------+
"""
-- Approach 1: Using where clause
SELECT E1.Name as Employee
FROM Employee E1, Employee E2
WHERE E1.ManagerId = E2.Id and E1.Salary > E2.Salary


-- Approach 2: Using join clause
-- More common and more efficient way to link tables
-- and you can use `on` to specify conditions 
SELECT E1.Name as Employee
FROM Employee E1 
JOIN Employee E2 on E1.ManagerId = E2.Id
AND E1.Salary > E2.Salary