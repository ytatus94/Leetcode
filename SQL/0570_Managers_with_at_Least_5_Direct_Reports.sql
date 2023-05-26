# 方法 1.
SELECT Name
FROM Employee
WHERE Id IN (
    SELECT ManagerId
    FROM Employee
    GROUP BY ManagerId
    HAVING COUNT(*) > 4
);

# 方法2. e1 是員工, e2 是主管
SELECT e2.Name
FROM Employee AS e1
JOIN Employee AS e2
ON e1.ManagerId = e2.Id
GROUP BY e2.Name
HAVING COUNT(e2.Name) >= 5;
