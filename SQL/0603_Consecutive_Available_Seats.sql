-- 座位要相鄰，所以編號差 1
-- 考會不會用 ABS()
SELECT DISTINCT c1.seat_id
FROM cinema AS c1
JOIN cinema AS c2
WHERE ABS(c1.seat_id - c2.seat_id) = 1
AND (c1.free = 1 AND c2.free = 1)
ORDER BY c1.seat_id;
