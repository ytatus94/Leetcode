# Write your MySQL query statement below
SELECT D.Name AS Department,
       E.Name AS Employee,
       Salary
FROM Employee E
JOIN Department D
ON E.DepartmentId = D.Id
WHERE (E.DepartmentId, E.Salary) IN (
    SELECT DepartmentId, MAX(Salary)
    FROM Employee
    GROUP BY DepartmentId
);


-- 先選出每個部門中最高的薪水
-- 合併表格後，利用上面的結果篩選出最後答案
SELECT d.name AS Department,
       e.name AS Employee,
       e.salary AS Salary
FROM Employee e
LEFT JOIN Department d
ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId,
           MAX(Salary) AS Salary
    FROM Employee
    GROUP BY departmentId
);
