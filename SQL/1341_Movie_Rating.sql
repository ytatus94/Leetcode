-- 方法 1.
WITH t AS (
    SELECT
        m.movie_id AS movie_id,
        m.title AS title,
        u.user_id AS user_id,
        u.name AS name,
        mr.rating AS rating,
        mr.created_at AS created_at
    FROM MovieRating AS mr
    JOIN Movies AS m
    JOIN Users AS u
    ON mr.movie_id = m.movie_id
    AND mr.user_id = u.user_id
)
SELECT t2.results
FROM (
    (SELECT
        name AS results,
        COUNT(name) AS cnt
    FROM t
    GROUP BY 1
    ORDER BY 2 DESC, 1 ASC
    LIMIT 1)
    UNION
    (SELECT
        title AS results,
        AVG(rating) AS avg_rating
    FROM t
    WHERE created_at BETWEEN '2020-02-01' AND '2020-02-28'
    GROUP BY 1
    ORDER BY 2 DESC, 1 ASC
    LIMIT 1)
) AS t2;

 方法 2.
(
    SELECT
        u.name AS results
    FROM Users AS u
    JOIN MovieRating AS mr
    ON u.user_id = mr.user_id
    GROUP BY 1
    ORDER BY COUNT(mr.rating) DESC, 1
    LIMIT 1
)
UNION ALL
(
    SELECT
        m.title AS results
    FROM Movies AS m
    JOIN MovieRating AS mr
    ON m.movie_id = mr.movie_id
    WHERE mr.created_at >= '2020-02-01'
    AND mr.created_at < '2020-03-01'
    GROUP BY 1
    ORDER BY AVG(rating) DESC, 1
    LIMIT 1
);
