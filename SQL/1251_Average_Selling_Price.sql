# Write your MySQL query statement below
SELECT
    p.product_id,
    ROUND(SUM(p.price * u.units) / SUM(u.units), 2) AS average_price
FROM Prices AS p
LEFT JOIN UnitsSold AS u
ON p.product_id = u.product_id AND
   (u.purchase_date BETWEEN p.start_date AND p.end_date)
GROUP BY 1
ORDER BY 1;