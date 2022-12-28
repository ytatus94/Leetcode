-- 考會不會用 window function
-- 注意 alias 中的 rank 要加上引號，不然會報錯，可能因為是要和 RANK() 函數區分開來的緣故
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank'
FROM Scores;
