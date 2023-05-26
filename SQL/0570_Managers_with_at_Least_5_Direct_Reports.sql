-- 考會不會 GROUP BY 和 HAVING
-- 方法 1.
SELECT Name
FROM Employee
WHERE Id IN (
    SELECT ManagerId
    FROM Employee
    GROUP BY ManagerId
    HAVING COUNT(*) > 4
);

-- 方法2. 把 e1 當員工, e2 當主管, 主管名字出現五次以上就是有五個員工向這個主管報告
SELECT e2.Name
FROM Employee AS e1
JOIN Employee AS e2
ON e1.ManagerId = e2.Id
GROUP BY e2.Name
HAVING COUNT(e2.Name) >= 5;
