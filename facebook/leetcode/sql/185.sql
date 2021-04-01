"""185. Department Top Three Salaries
https://leetcode.com/problems/department-top-three-salaries/

Write a SQL query to find employees who earn the top three salaries in each of the department. 
For the above tables, your SQL query should return the following rows (order of rows does not matter).

Employee table:
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
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
| IT         | Randy    | 85000  |
| IT         | Joe      | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+
"""
SELECT Department, Employee, Salary
FROM (
    SELECT 
        Department.name AS Department,
        Employee.name AS Employee,
        Employee.Salary,
        DENSE_RANK() OVER (
            PARTITION BY Department.name 
            ORDER BY Employee.salary DESC
        ) as dept_salary_rank
    FROM Employee JOIN Department on Employee.DepartmentId = Department.Id
) x where x.dept_salary_rank <= 3 -- not accessible from the inner query, this is why it's here
