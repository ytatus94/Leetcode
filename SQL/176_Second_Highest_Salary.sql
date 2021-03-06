# 有可能沒有第二高的薪水，這時候要傳回 null
SELECT (SELECT DISTINCT Salary
        FROM Employee
        ORDER BY 1 DESC
        LIMIT 1
        OFFSET 1) AS SecondHighestSalary;

# 方法二:
SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary)
                FROM Employee);
