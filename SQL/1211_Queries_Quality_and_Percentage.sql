# 方法 1.
# Write your MySQL query statement below
SELECT
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(SUM(IF(rating < 3, 1, 0)) / COUNT(rating) * 100., 2) AS poor_query_percentage
FROM Queries
GROUP BY 1;

# 方法 2.
# Write your MySQL query statement below
SELECT
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(AVG(rating < 3) * 100., 2) AS poor_query_percentage
FROM Queries
GROUP BY 1;
