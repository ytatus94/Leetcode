-- 考會不會用 window function
-- 注意 alias 中的 rank 要加上雙引號
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS "rank"
FROM Scores
