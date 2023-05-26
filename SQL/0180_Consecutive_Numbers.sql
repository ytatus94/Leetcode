-- 考會不會做 self-join
-- 如果用 FROM 來 join 表格，那連接的條件就用 WHERE，而且這種方式的 join 是 inner join

-- 把 Logs 表格做 self-join
-- 注意 WHERE 部分的寫法，這樣可以確定三個 id 是連續的
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs AS l1, Logs AS l2, Logs AS l3
WHERE l1.id + 1 = l2.id AND l2.id + 1 = l3.id
AND l1.num = l2.num AND l2.num = l3.num;

# 方法 2.
# Write your MySQL query statement below
SELECT
    DISTINCT l1.num AS ConsecutiveNums
FROM Logs AS l1, Logs AS l2, Logs AS l3 
WHERE
    l1.id = l2.id - 1 AND l2.id = l3.id - 1 AND
    l1.num = l2.num AND l2.num = l3.num;
