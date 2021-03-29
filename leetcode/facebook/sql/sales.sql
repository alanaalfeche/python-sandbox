/*
https://leetcode.com/discuss/interview-question/807990/Facebook-SQL-questions-DE

sales
+------------------+---------
| product_id | INTEGER
| store_id | INTEGER |
| customer_id | INTEGER |
| promotion_id | INTEGER |
| store_sales | DECIMAL |
| store_cost | DECIMAL |
| units_sold | DECIMAL |
| transaction_date | DATE |

products
+------------------+---------
| product_id | INTEGER |
| product_class_id | INTEGER |
| brand_name | VARCHAR |
| product_name | VARCHAR |
| is_low_fat_flg | TINYINT |
| is_recyclable_flg | TINYINT |
| gross_weight | DECIMAL |
| net_weight | DECIMAL |

promotions |
+------------------+---------+
| promotion_id | INTEGER|
| promotion_name | VARCHAR |
| media_type | VARCHAR |
| cost | DECIMAL |
| start_date | DATE |
| end_date | DATE |

product_classes
+------------------+---------+
| product_class_id | INTEGER |
| product_subcategory | VARCHAR |
| product_category | VARCHAR |
| product_department | VARCHAR |
| product_family | VARCHAR |
*/

-- Q1. What perecentage of products have both low fat and recycable?
SELECT ROUND(
    AVG(
        CASE 
            WHEN is_low_fat_flg = 1 AND is_recyclable_flg = 1
            THEN 1
            ELSE 0
        END
    )
, 2) AS PERCENTAGE
FROM PRODUCTS

-- Q2. Find top 5 sales products having promotions.
SELECT product_id -- , SUM(store_sales) AS total_sales
FROM sales
WHERE promotion_id IS NOT NULL
GROUP BY product_id
ORDER BY units_sold DESC -- SUM(UNITS_SOLD * STORE_COST)
LIMIT 5

-- Q3. What percentage of sales happened on first and last day for all promotions?
SELECT ROUND(
    AVG(
        CASE
            WHEN MIN(start_date) = transaction_date THEN 1
            WHEN MAX(start_date) = transaction_date THEN 1
            ELSE 0
        END
    )
, 2) AS PERCENTAGE
FROM sales
JOIN promotions on sales.promotion_id = promotions.promotion_id

-- Q4. Which product had the highest sales with promotions and sales?
SELECT product_id
FROM sales
JOIN promotions on sales.promotion_id = promotions.promotion_id
GROUP BY product_id
ORDER BY SUM(units_sold * store_cost) - cost DESC
LIMIT 1

-- Q5. What are the top five (ranked in decreasing order) single-channel media types that correspond to the most money the grocery chain had spent on its promotional campaigns?
SELECT media_type
FROM promotions
GROUP BY media_type
ORDER BY SUM(cost) DESC
LIMIT 5

-- Q6. Return the proportion of valid sales that occurred on certain dates.
SELECT ROUND(
    AVG(
        CASE
            WHEN transaction_date = 'certain_date' THEN 1
            ELSE 0
        END
    )
, 2) AS PERCENTAGE
FROM sales
GROUP BY transaction_date

-- Q7. Manager want to analyze the how the promotions on certain products are performing. Calculate percent of promoted sales.
SELECT ROUND(
    AVG(
        CASE
            WHEN promotion_id is NOT NULL THEN 1
            ELSE 0
        END
    )
)
FROM sales

-- Q8. Find the Top 3 product product_class_id by the total sales.
SELECT product_class_id
FROM products
JOIN sales on products.product_id = sales.product_id
GROUP BY product_class_id
ORDER BY SUM(units_sold * store_cost) DESC
LIMIT 3