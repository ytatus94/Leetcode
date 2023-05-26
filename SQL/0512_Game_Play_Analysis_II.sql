-- 先用 sub query 找出每個使用者最早登入的時間
-- 再用 WHERE 篩選，並顯示該使用者在第一次登入時使用的設備
SELECT
    A1.player_id,
    A1.device_id
FROM Activity A1
WHERE (A1.player_id, A1.event_date) IN (
    SELECT
      A2.player_id,
      MIN(A2.event_date)
    FROM Activity A2
    GROUP BY A2.player_id
);
