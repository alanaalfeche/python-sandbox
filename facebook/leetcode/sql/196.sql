"""196. Delete Duplicate Emails
https://leetcode.com/problems/delete-duplicate-emails/

Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+

Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
"""
-- Approach 1: https://stackoverflow.com/questions/45494/mysql-error-1093-cant-specify-target-table-for-update-in-from-clause
DELETE FROM Person
WHERE Id NOT IN
    (SELECT * FROM ( -- does not work without this extra wrapper
        SELECT MIN(Id)
        FROM Person
        GROUP BY Email
    ) AS X
);

-- Approach 2: Use join
DELETE P1 FROM Person P1, Person P2
WHERE P1.Email = P2.Email AND P1.Id > P2.Id