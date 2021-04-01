"""1204. Last Person to Fit in the Elevator
https://leetcode.com/problems/last-person-to-fit-in-the-elevator/

The maximum weight the elevator can hold is 1000.

Write an SQL query to find the person_name of the last person who will fit in the elevator without exceeding the weight limit. 
It is guaranteed that the person who is first in the queue can fit in the elevator.

Queue table
+-----------+-------------------+--------+------+
| person_id | person_name       | weight | turn |
+-----------+-------------------+--------+------+
| 5         | George Washington | 250    | 1    |
| 3         | John Adams        | 350    | 2    |
| 6         | Thomas Jefferson  | 400    | 3    |
| 2         | Will Johnliams    | 200    | 4    |
| 4         | Thomas Jefferson  | 175    | 5    |
| 1         | James Elephant    | 500    | 6    |
+-----------+-------------------+--------+------+

Result table
+-------------------+
| person_name       |
+-------------------+
| Thomas Jefferson  |
+-------------------+
"""
SELECT person_name
FROM (
    SELECT 
        person_name,
        SUM(weight) OVER (ORDER BY turn) AS weight
    FROM queue
) q
WHERE weight <= 1000
ORDER BY WEIGHT DESC LIMIT 1