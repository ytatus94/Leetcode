-- 就是要知道怎麼選定時間範圍
-- 2019-07-27 是第 30 天，那往前推 2019-06-28 是第一天
-- INTERVAL 29 DAY 是因為要包含頭尾，所以只有 29 天的差別

-- 方法1
SELECT activity_date AS day,
       COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN ("2019-07-27" - INTERVAL 29 DAY) AND "2019-07-27"
GROUP BY 1
ORDER BY 1;

-- 方法2
SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date >= '2019-06-28' AND activity_date <= '2019-07-27'
GROUP BY 1
ORDER BY 1;

-- 
# Write your MySQL query statement below
SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 29 DAY) AND '2019-07-27'
GROUP BY 1
