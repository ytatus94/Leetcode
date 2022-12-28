-- 這題考會不會用 GROUP BY 和 HAVING
SELECT class
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;
