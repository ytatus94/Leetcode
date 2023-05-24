# 方法 1.
# Write your MySQL query statement below
SELECT p.product_name, s.year, s.price
FROM Sales s
JOIN Product p
ON s.product_id = p.product_id
ORDER BY 1

# 方法 2.
# Write your MySQL query statement below
SELECT p.product_name, s.year, s.price
FROM Sales AS s, Product AS p
WHERE s.product_id = p.product_id
ORDER BY 1
