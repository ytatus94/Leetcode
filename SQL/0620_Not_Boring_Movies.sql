-- 用 id % 2 來判斷是否是奇數 
SELECT *
FROM cinema
WHERE id % 2 <> 0
AND description <> 'boring'
ORDER BY rating DESC;
