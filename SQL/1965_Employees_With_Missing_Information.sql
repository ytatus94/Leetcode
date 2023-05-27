-- 方法 1
-- 不能用 FULL OUTER JOIN 因為會在 employee_id 欄位產生空值
-- UNION 會消除重複的欄位，且合併後的都叫 employee_id 所以可以直接拿來排序
SELECT e.employee_id
FROM Employees AS e
LEFT JOIN Salaries AS s
ON e.employee_id = s.employee_id
WHERE s.salary IS NULL
UNION
SELECT s.employee_id
FROM Salaries AS s
LEFT JOIN Employees AS e
ON s.employee_id = e.employee_id
WHERE e.name IS NULL
ORDER BY employee_id;

-- 方法 2:
SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (
    SELECT employee_id
    FROM Salaries
)
UNION
SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (
    SELECT employee_id
    FROM Employees
)
ORDER BY employee_id;
