-- 要會用 IFNULL(expression, alt_value) 判斷是不是 NULL 如果是 NULL 就設成 alt_value
-- 在 sub query 中計算 2019 年每個 buyer 有多少交易，沒有交易的會顯示 NULL

SELECT
    u.user_id AS buyer_id,
    u.join_date AS join_date,
    IFNULL(o.orders_in_2019, 0) AS orders_in_2019
FROM Users AS u
LEFT JOIN (
    SELECT
        buyer_id,
        COUNT(*) AS orders_in_2019
    FROM Orders o
    WHERE order_date >= '2019-01-01' AND order_date <= '2019-12-31'
    GROUP BY 1
) AS o
ON u.user_id = o.buyer_id;
