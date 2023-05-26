-- 有些員工沒有 bonus, 這些人也要列入考慮
-- 所以要加上 B.bonus IS NULL 才可以
SELECT E.name, B.bonus
FROM Employee E
LEFT JOIN Bonus B
ON E.empId = B.empId
WHERE B.bonus < 1000 OR B.bonus IS NULL;
