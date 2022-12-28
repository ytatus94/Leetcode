-- 先用 DENSE_RANK() 對每個部門的薪水做降冪排序，注意 alias 的 rank 要用引號括起來
-- window function 不能用在 WHERE, GROUP BY, HAVING 裡面
-- 在和 Department 表格做 JOIN 選出排名前三名的薪水
SELECT d.name AS Department,
       e.name AS Employee,
       e.salary AS Salary
FROM (
    SELECT departmentId,
           name,
           salary,
           DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS 'rank'
    FROM Employee
) e
JOIN Department d
ON e.departmentId = d.id
WHERE e.rank <= 3
