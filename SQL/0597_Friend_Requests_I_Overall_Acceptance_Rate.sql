-- IFNULL(expression, alt_value) 判斷 expression 是不是 NULL
-- 如果不是, 傳回 expression 的結果
-- 如果是, 傳回 alt_value
SELECT IFNULL(ROUND((SELECT COUNT(DISTINCT requester_id, accepter_id)
                     FROM request_accepted) /
                    (SELECT COUNT(DISTINCT sender_id, send_to_id)
                     FROM friend_request), 2), 0) AS accept_rate;
