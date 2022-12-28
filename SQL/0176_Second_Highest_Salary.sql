-- 方法1. 有可能沒有第二高的薪水，這時候要傳回 null
-- 要會用 OFFSET N，表格開頭的前 N 行就刪掉
-- 注意 LIMIT 寫在 OFFSET N 前面，但是執行時是先執行 OFFSET N 再執行 LIMIT
-- 最外面還要再用一個 SELECT 包起來，才能顯示 null (不包起來 null 會顯示成空白)
SELECT (
    SELECT DISTINCT Salary
    FROM Employee
    ORDER BY 1 DESC
    LIMIT 1
    OFFSET 1
) AS SecondHighestSalary;

-- 方法2.
-- WHERE 中的 query 會先執行，所以先找出最高的薪水
-- 再從 Employee 中找出滿足 WHERE 條件的部分，這樣找出來的薪水都比最高薪還低
-- 最後再用第一行的 SELECT 顯示出要看的欄位，選出剩下的表格中最高薪，這樣就是全部表格中的第二高薪
SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (
    SELECT MAX(Salary)
    FROM Employee
);
                
