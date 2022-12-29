-- 這一題只要知道 GROUP_CONCAT() 就能解決
-- GROUP_CONCAT(expr) 是 MySQL 才支援的函數
SELECT sell_date,
       COUNT(DISTINCT product) AS num_sold,
       GROUP_CONCAT(DISTINCT product ORDER BY product ASC SEPARATOR ',') as products      
FROM Activities
GROUP BY 1
ORDER BY 1
