-- 考 WHERE 和 OR
SELECT name
FROM customer
WHERE referee_id <> 2 OR referee_id IS NULL;
