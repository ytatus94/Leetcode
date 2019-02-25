SELECT name
FROM salesperson
WHERE sales_id NOT IN (SELECT o.sales_id
                       FROM orders AS o
                       JOIN company AS c
                       ON o.com_id = c.com_id
                       WHERE o.name = 'RED');
