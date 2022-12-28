-- 考 GROUP BY 和 ORDER BY 還有會不會降冪排序
SELECT customer_number
FROM orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
