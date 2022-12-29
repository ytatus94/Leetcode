-- CASE WHEN ... THEN ... ELSE ... END
-- 要會算 mod 和要會通配符
SELECT
    employee_id,
    CASE
        WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary 
        ELSE 0 
    END AS bonus
FROM Employees
ORDER BY 1;
