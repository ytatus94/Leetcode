-- 考會不會用 aggregate function 做計算，還有會不會用 ROUND() 函數
-- CASE 述句會產生一個新的欄位，當 status 有 cancelled 的話，新欄位的值就會是 1 沒有的話就是 0
-- 然後 GROUP BY 時會把這個新欄位加起來，再除以總 row 數目 (用 COUNT 算出來)
-- 最後用 ROUND() 取小數點後兩位數
SELECT
    request_at AS Day,
    ROUND(SUM(CASE WHEN status LIKE 'cancelled%' THEN 1 ELSE 0 END) / COUNT(request_at), 2) AS 'Cancellation Rate'
FROM Trips
WHERE client_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
AND driver_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at;
