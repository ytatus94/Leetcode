SELECT
    CASE
        WHEN MOD(id, 2) = 1 AND id = counts THEN id
        WHEN MOD(id, 2) = 1 AND id != counts THEN id+1
        ELSE id-1
    END AS id,
    student
FROM seat, (SELECT COUNT(*) AS counts
            FROM seat) AS seat_counts
ORDER BY id ASC
