"""1212. Team Scores in Football Tournament
https://leetcode.com/problems/team-scores-in-football-tournament/

Table: Teams
+---------------+----------+
| Column Name   | Type     |
+---------------+----------+
| team_id       | int      |
| team_name     | varchar  |
+---------------+----------+

Table: Matches
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| match_id      | int     |
| host_team     | int     |
| guest_team    | int     | 
| host_goals    | int     |
| guest_goals   | int     |
+---------------+---------+

You would like to compute the scores of all teams after all matches. Points are awarded as follows:
A team receives three points if they win a match (Score strictly more goals than the opponent team).
A team receives one point if they draw a match (Same number of goals as the opponent team).
A team receives no points if they lose a match (Score less goals than the opponent team).

Write an SQL query that selects the team_id, team_name and num_points of each team in the tournament after all described matches. 
Result table should be ordered by num_points (decreasing order). In case of a tie, order the records by team_id (increasing order).

Result table:
+------------+--------------+---------------+
| team_id    | team_name    | num_points    |
+------------+--------------+---------------+
| 10         | Leetcode FC  | 7             |
| 20         | NewYork FC   | 3             |
| 50         | Toronto FC   | 3             |
| 30         | Atlanta FC   | 1             |
| 40         | Chicago FC   | 0             |
+------------+--------------+---------------+
"""
WITH points_cte AS (
    SELECT 
        host_team team_id,
        CASE 
            WHEN host_goals > guest_goals THEN 3
            WHEN host_goals = guest_goals THEN 1
            ELSE 0
        END points
    FROM matches

    UNION ALL
    
    SELECT 
        guest_team team_id,
        CASE
            WHEN guest_goals > host_goals THEN 3
            WHEN guest_goals = host_goals THEN 1
            ELSE 0
        END points
    FROM matches
)

SELECT team_id, team_name, SUM(IFNULL(points, 0)) as num_points
FROM teams
LEFT JOIN points_cte USING (team_id)
GROUP BY team_id
ORDER BY num_points DESC, team_id