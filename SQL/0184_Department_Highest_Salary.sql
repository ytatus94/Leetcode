SELECT
    D.Name AS Department,
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


-- 先在 sub query 中選出每個部門中最高的薪水
-- 合併表格後，利用上面的結果篩選出最後答案
-- sub query 中傳回的是兩個欄位的表格，所以 WHERE 子句中要用兩個欄位 (e.departmentId, e.salary) 來比較
SELECT
    d.name AS Department,
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

-- 用了 window function 跑很慢
SELECT
    sub.Department,
    sub.Employee,
    sub.Salary
FROM (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        MAX(e.salary) OVER (PARTITION BY d.name) AS max_salary
    FROM Employee e
    LEFT JOIN Department d
    ON e.departmentId = d.id
) sub
WHERE sub.Salary = sub.max_salary;
