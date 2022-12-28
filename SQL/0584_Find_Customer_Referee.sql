-- 考 WHERE 和 OR
-- 注意"不等於"是用 <> (雖然用 != 也可以)
SELECT name
FROM customer
WHERE referee_id <> 2 OR referee_id IS NULL;
