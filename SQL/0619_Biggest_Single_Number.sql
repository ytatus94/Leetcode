-- num 可能會有重複，要先找出不重複的 num，再從這些裡面找出最大的數值

-- 方法 1.
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM number
    GROUP BY num
    HAVING COUNT(*) = 1
) AS t;

-- 方法 2.
SELECT
    MAX(t.num) AS num
FROM (
    SELECT
        num,
        COUNT(num) AS cnt
    FROM MyNumbers
    GROUP BY 1
) AS t
WHERE cnt = 1;
