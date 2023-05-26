-- 要會 DATE_ADD(date, INTERVAL x DAY) 的用法, 把 date + x 天
-- 先用 subquery 找出在第一天登入後，隔天也登入的玩家
-- 第二天也登入的玩家數目 / 全部玩家數目 = 比例
-- 注意 Activity 中 player_id 會重複，所以要用 DISTINCT
SELECT
    ROUND(COUNT(player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity
WHERE (player_id, event_date) IN (
    SELECT
        player_id,
        DATE_ADD(MIN(event_date), INTERVAL 1 DAY)
    FROM Activity
    GROUP BY 1
);
