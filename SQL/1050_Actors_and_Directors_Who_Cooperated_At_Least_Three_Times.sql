-- 這一題其實是在考會不會用 HAVING

-- 方法1
SELECT
    actor_id,
    director_id
FROM (
    SELECT
        actor_id,
        director_id,
        COUNT(*) AS cnt
    FROM ActorDirector
    GROUP BY 1, 2
) sub
WHERE cnt >= 3

-- 方法2 比較快
SELECT
    actor_id,
    director_id
FROM ActorDirector
GROUP BY 1, 2
HAVING COUNT(1) >= 3
