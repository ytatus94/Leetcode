-- 這題考會不會用 GROUP BY 和 HAVING
-- 因為 HAVING 是篩選，所以後面接的一定是條件判斷
SELECT class
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;
