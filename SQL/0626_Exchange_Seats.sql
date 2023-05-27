-- 方法 1. 用 CASE
SELECT
    CASE
        WHEN MOD(id, 2) = 1 AND id = counts THEN id
        WHEN MOD(id, 2) = 1 AND id != counts THEN id+1
        ELSE id-1
    END AS id,
    student
FROM seat, (SELECT COUNT(*) AS counts
            FROM seat) AS seat_counts
ORDER BY id ASC;

-- 方法 2. 用 IF
-- 如果最後一個 id 是奇數, 就不變 (id = id)
-- 如果 id 是奇數, 就 id = id+1
-- 如果 id 是偶數, 就 id = id-1
SELECT
    IF(id % 2 = 1, IF(id = (SELECT COUNT(*) FROM Seat), id, id + 1), id - 1) AS id,
    student
FROM Seat
ORDER BY id ASC;
