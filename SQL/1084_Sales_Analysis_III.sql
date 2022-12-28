-- 合併 product 和 sales 表格，選出符合 Q1 的
-- 但是要找出只有在 Q1 有賣出的產品，所以在 sub query 中
-- 要找出在 Q1 以外的時間賣出的產品，然後排除掉這些
-- 產品可能被賣掉很多次，所以需要用 DISTINCT

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
ORDER BY p.product_id;
