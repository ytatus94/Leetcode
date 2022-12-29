-- 要知道怎麼篩選出沒有交易的客戶
-- 合併表格，選出沒有交易的客戶，最後計算數目
SELECT v.customer_id,
       COUNT(v.customer_id) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY 1;
