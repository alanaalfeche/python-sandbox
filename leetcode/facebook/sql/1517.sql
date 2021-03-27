""" 1517. Find Users With Valid E-Mails

Write an SQL query to find the users who have valid emails.

A valid e-mail has a prefix name and a domain where: 
- The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.' and/or dash '-'. 
- The prefix name must start with a letter.
- The domain is '@leetcode.com'.

Users:
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 2       | Jonathan  | jonathanisgreat         |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
| 5       | Marwan    | quarz#2020@leetcode.com |
| 6       | David     | david69@gmail.com       |
| 7       | Shapiro   | .shapo@leetcode.com     |
+---------+-----------+-------------------------+

Result table:
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
+---------+-----------+-------------------------+

"""

SELECT *
FROM Users
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_.-]*@leetcode.com$';
-- ^ must start with a letter
-- * can be any number, including zero
-- $ must end with