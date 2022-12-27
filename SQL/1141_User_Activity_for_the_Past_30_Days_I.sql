-- 方法1
SELECT activity_date AS day,
       COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN ("2019-07-27" - INTERVAL 29 DAY) AND "2019-07-27"
GROUP BY 1
ORDER BY 1

-- 方法2
SELECT activity_date AS day,
       COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date >= '2019-06-28' AND activity_date <= '2019-07-27'
GROUP BY 1
ORDER BY 1
