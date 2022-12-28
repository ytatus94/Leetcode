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

-- 方法2 是 leetcode 提供的答案
-- 合併 Employee 和 Department 後得到 (先不做任何篩選)
+----+-------+--------+--------------+----------------+
| id | name  | salary | departmentId | departmentName |
+----+-------+--------+--------------+----------------+
| 1  | Joe   | 85000  | 1            | IT             |
| 2  | Henry | 80000  | 2            | Sales          |
| 3  | Sam   | 60000  | 2            | Sales          |
| 4  | Max   | 90000  | 1            | IT             |
| 5  | Janet | 69000  | 1            | IT             |
| 6  | Randy | 85000  | 1            | IT             |
| 7  | Will  | 70000  | 1            | IT             |
+----+-------+--------+--------------+----------------+
-- 要找每個部門的前三高的薪水，就一 row 一 row 的看，計算在同一部門中有多少薪水比當前 row 的薪水高
-- 這就是 WHERE 中 sub query 在做的事情
-- 部門做高薪 --> 0 row 比當前高，部門第二高薪 --> 只有 1 row 比當前高，部門第三高薪 --> 只有 2 row 比當前高
-- 所以 WHERE 就用 3 > 多少薪水比當前高
SELECT
    d.Name AS 'Department',
    e1.Name AS 'Employee',
    e1.Salary
FROM Employee e1
JOIN Department d 
ON e1.DepartmentId = d.Id
WHERE 3 > ( -- 這裡的 3 是數字 3 不是 SELECT 中的第三個欄位
    SELECT COUNT(DISTINCT e2.Salary)
    FROM Employee e2
    WHERE e2.Salary > e1.Salary AND e1.DepartmentId = e2.DepartmentId
);
