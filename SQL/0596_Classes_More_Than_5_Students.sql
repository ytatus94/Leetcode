-- 這題考會不會用 GROUP BY 和 HAVING
-- 因為 HAVING 是篩選，所以後面接的一定是條件判斷
-- 而且 HAVING 後面接的一定是 Aggregate Function
SELECT class
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;
