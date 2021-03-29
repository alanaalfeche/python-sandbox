""" 1270. All People Report to the Given Manager 

Write an SQL query to find employee_id of all employees that directly or indirectly report their work to the head of the company.

The indirect relation between managers will not exceed 3 managers as the company is small.

Return result table in any order without duplicates.

Employees table:
+-------------+---------------+------------+
| employee_id | employee_name | manager_id |
+-------------+---------------+------------+
| 1           | Boss          | 1          |
| 3           | Alice         | 3          |
| 2           | Bob           | 1          |
| 4           | Daniel        | 2          |
| 7           | Luis          | 4          |
| 8           | Jhon          | 3          |
| 9           | Angela        | 8          |
| 77          | Robert        | 1          |
+-------------+---------------+------------+

Result table:
+-------------+
| employee_id |
+-------------+
| 2           |
| 77          |
| 4           |
| 7           |
+-------------+
"""
-- Approach 1. Use 3 joines because indirect relation does not exceed 3 managers
SELECT e1.employee_id as employee_id
FROM Employees e1
JOIN Employees e2 on e1.manager_id = e2.employee_id
JOIN Employees e3 on e2.manager_id = e3.employee_id
WHERE e3.manager_id = 1 and e1.employee_id != 1

-- Approach 2. Use recursive CTE
"""
WITH expression_name (column_list)
AS
(
    -- Anchor member: returns the base result of the CTE
    initial query
    UNION ALL
    -- Recursive member that references expression_name
    recursive query
)
-- references expression name
SELECT * 
FROM expression_name
"""
WITH recursive cte AS (
    SELECT 
        employee_id
    FROM 
        Employees
    WHERE manager_id = 1 and employee_id != 1

    UNION ALL

    SELECT 
        e1.employee_id
    FROM 
        Employees e1
        JOIN cte e2
            ON (e2.employee_id = e1.manager_id)
)
SELECT employee_id
FROM cte;
