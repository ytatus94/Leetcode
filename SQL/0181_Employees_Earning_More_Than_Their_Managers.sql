-- 考會不會 self-join
SELECT E1.Name AS Employee
FROM Employee E1
LEFT JOIN Employee E2
ON E1.ManagerID = E2.Id
WHERE E1.ManagerID IS NOT NULL
AND E1.Salary > E2.Salary;
