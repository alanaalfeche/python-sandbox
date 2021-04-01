"""1757. Recyclable and Low Fat Products
https://leetcode.com/problems/recyclable-and-low-fat-products/

Write an SQL query to find the ids of products that are both low fat and recyclable.

Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+

Result table:
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
"""
SELECT product_id
FROM products
WHERE low_fats = 'Y' AND recyclable = 'Y';

-- Follow Up: Write a query to get the percentage of certain products
SELECT ROUND(
        AVG(CASE 
                WHEN low_fats = 'Y' OR recyclable = 'Y' 
                THEN 1 
                ELSE 0 
            END)
        ,2) AS PERCENTAGE
FROM products
