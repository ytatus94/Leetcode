-- 考會不會 JOIN 還有會不會做數學計算
SELECT s1.stock_name,
       s1.price * -1 + s2.price AS capital_gain_loss
FROM (
    SELECT stock_name,
           SUM(price) AS price
    FROM Stocks
    WHERE operation = 'Buy'
    GROUP BY stock_name
) AS s1
JOIN (
    SELECT stock_name,
           SUM(price) AS price
    FROM Stocks
    WHERE operation = 'Sell'
    GROUP BY stock_name
) AS s2
ON s1.stock_name = s2.stock_name;
