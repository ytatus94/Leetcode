SELECT
    DISTINCT p.product_id AS product_id,
    p.product_name AS product_name
FROM Product AS p
LEFT JOIN Sales AS s
ON p.product_id = s.product_id
WHERE sale_date >= '2019-01-01' AND sale_date <= '2019-03-31'
AND p.product_id NOT IN (
    SELECT DISTINCT product_id
    FROM Sales
    WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31'
)
ORDER BY p.product_id
