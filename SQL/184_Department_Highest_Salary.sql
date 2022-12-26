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
