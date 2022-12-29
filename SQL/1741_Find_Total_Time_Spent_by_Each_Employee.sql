-- 要會用 SUM(), GROUP BY
-- 有 GROUP BY 就要有 aggregation function 欄位
SELECT
    event_day AS day,
    emp_id,
    SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY 1, 2;
