-- 要會用 COUNT(), GROUP BY, ORDER BY
-- 有 GROUP BY 就一定要有欄位用到 aggregation function
SELECT
    user_id,
    COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY 1
ORDER BY 1
