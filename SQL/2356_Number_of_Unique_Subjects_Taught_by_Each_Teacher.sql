-- 要 unique subject 所以記得要加上 DISTINCT
SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY 1
ORDER BY 1;
