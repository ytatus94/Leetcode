-- 如果把 p1 p2 合併，不做任何篩選，會得到
+----+------------------++----+
| id | email            || id |
+----+------------------++----+
| 1  | john@example.com || 1  |
| 1  | john@example.com || 3  |
| 2  | bob@example.com  || 2  |
| 3  | john@example.com || 1  | v
| 3  | john@example.com || 3  |
+----+------------------++----+
-- 如果加上篩選條件 p1.Id > p2.Id 那只有 v 那 row 會留下
-- 所以刪除時會從 p1 中把 v 那 row 刪除
DELETE p1
FROM Person AS p1 
JOIN Person AS p2
ON p1.Email = p2.Email AND p1.Id > p2.Id;

-- 先選出每個 email 中最小的 id
-- 再把不是這些 id 的 rows 刪除
-- 需要多一個 SELECT * FROM() AS p 是因為不能在 Person 中刪除依照 Person Query 出來的結果
-- 所以先產生一個 p 就沒事
DELETE FROM Person
WHERE id NOT IN (
    SELECT *
    FROM (
        SELECT MIN(id)
        FROM Person
        GROUP BY email
    ) AS p
);
