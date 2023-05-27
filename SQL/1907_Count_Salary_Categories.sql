-- 分開成 3 種情況討論，再用 UNION 結合起來
SELECT 
    'High Salary' AS category,
    COUNT(*) AS accounts_count
FROM Accounts
WHERE income > 50000
UNION
SELECT 
    'Low Salary' AS category,
    COUNT(*) AS accounts_count
FROM Accounts
WHERE income < 20000
UNION
SELECT 
    'Average Salary' AS category,
    COUNT(*) AS accounts_count
FROM Accounts
WHERE income BETWEEN 20000 AND 50000;

-- 這題如果用 CASE 子句產生 category 再 group by 起來，計算數目的話
-- 因為表格內沒有符合 Average Salary 的紀錄，group by 之後表格內不會有 Average Salary 的結果
-- 所以不能用這個方式
