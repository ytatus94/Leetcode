SELECT MAX(num) AS num
FROM (SELECT num
      FROM number
      GROUP BY num
      HAVING COUNT(*) = 1) AS t;

# 方法 2.
# Write your MySQL query statement below
SELECT
    MAX(t.num) AS num
FROM (
    SELECT
        num,
        COUNT(num) AS cnt
    FROM MyNumbers
    GROUP BY 1
) AS t
WHERE cnt = 1

