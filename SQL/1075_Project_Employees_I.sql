# Write your MySQL query statement below
SELECT project_id,
       ROUND(SUM(e.experience_years) / COUNT(e.employee_id), 2) average_years
FROM Project AS p, Employee AS e
WHERE p.employee_id = e.employee_id
GROUP BY 1
