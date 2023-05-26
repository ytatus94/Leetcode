-- 考 GROUP BY 和 aggregate function
SELECT
    player_id,
    MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
