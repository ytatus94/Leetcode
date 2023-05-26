-- 先找出有來自 RED 公司訂單的 sales_id
-- 然後排除這些 sales_id 就是答案
SELECT name
FROM salesperson
WHERE sales_id NOT IN (
    SELECT o.sales_id
    FROM orders AS o
    JOIN company AS c
    ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);
