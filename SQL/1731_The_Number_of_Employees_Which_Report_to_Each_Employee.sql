# Write your MySQL query statement below
SELECT
    e1.reports_to AS employee_id,
    e2.name,
    COUNT(e1.reports_to) AS reports_count,
    ROUND(AVG(e1.age)) AS average_age
FROM Employees AS e1
JOIN Employees AS e2
ON e1.reports_to = e2.employee_id
GROUP BY 1
ORDER BY 1;
