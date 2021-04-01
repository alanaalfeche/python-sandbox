"""1412. Find the Quiet Students in All Exams
https://leetcode.com/problems/find-the-quiet-students-in-all-exams/

A 'quite' student is the one who took at least one exam and didn't score neither the high score nor the low score.
Write an SQL query to report the students (student_id, student_name) being 'quiet' in ALL exams.
Don't return the student who has never taken any exam. Return the result table ordered by student_id.

Student table:
+-------------+---------------+
| student_id  | student_name  |
+-------------+---------------+
| 1           | Daniel        |
| 2           | Jade          |
| 3           | Stella        |
| 4           | Jonathan      |
| 5           | Will          |
+-------------+---------------+

Exam table:
+------------+--------------+-----------+
| exam_id    | student_id   | score     |
+------------+--------------+-----------+
| 10         |     1        |    70     |
| 10         |     2        |    80     |
| 10         |     3        |    90     |
| 20         |     1        |    80     |
| 30         |     1        |    70     |
| 30         |     3        |    80     |
| 30         |     4        |    90     |
| 40         |     1        |    60     |
| 40         |     2        |    70     |
| 40         |     4        |    80     |
+------------+--------------+-----------+

Result table:
+-------------+---------------+
| student_id  | student_name  |
+-------------+---------------+
| 2           | Jade          |
+-------------+---------------+
"""

WITH cte AS (
    SELECT 
        exam.student_id, 
        student_name,
        RANK() OVER ( -- dense_rank() will work too
            PARTITION BY exam_id
            ORDER BY score 
        ) asc_rank,
        RANK() OVER ( -- dense_rank() will work too
            PARTITION BY exam_id
            ORDER BY score
            DESC
        ) desc_rank
    FROM exam
    LEFT JOIN student on exam.student_id = student.student_id
)

SELECT DISTINCT student_id, student_name -- a student can take many test and get middle score all the time
FROM cte -- only return students that took a test
WHERE student_id NOT IN (
    SELECT student_id
    FROM cte
    WHERE asc_rank = 1 or desc_rank = 1
)
ORDER BY student_id