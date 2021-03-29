""" 597. Friend Requests I: Overall Acceptance Rate
Write an SQL query to find the overall acceptance rate of requests, which is the number of acceptance divided by the number of requests. 

Return the answer rounded to 2 decimals places.

FriendRequest table:
+-----------+------------+--------------+
| sender_id | send_to_id | request_date |
+-----------+------------+--------------+
| 1         | 2          | 2016/06/01   |
| 1         | 3          | 2016/06/01   |
| 1         | 4          | 2016/06/01   |
| 2         | 3          | 2016/06/02   |
| 3         | 4          | 2016/06/09   |
+-----------+------------+--------------+

RequestAccepted table:
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
| 3            | 4           | 2016/06/10  |
+--------------+-------------+-------------+

Result table:
+-------------+
| accept_rate |
+-------------+
| 0.8         |
+-------------+
"""
SELECT
    ROUND (
        IFNULL (
            (SELECT COUNT(DISTINCT requester_id, accepter_id) FROM RequestAccepted) /
            (SELECT COUNT(DISTINCT sender_id, send_to_id) FROM FriendRequest)
            , 0
        ), 2
    ) as accept_rate

-- Follow Up 1: Could you write a query to return the acceptance rate for every month?
-- Follow Up 2: Could you write a query to return the cumulative acceptance rate for every day?
