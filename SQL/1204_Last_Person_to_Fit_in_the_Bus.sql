# 方法 1.
# Write your MySQL query statement below
SELECT
    person_name
FROM Queue AS q1
WHERE (
    SELECT SUM(weight)
    FROM Queue AS q2
    WHERE q2.turn <= q1.turn
    ORDER BY turn
) <= 1000
ORDER BY q1.turn DESC
LIMIT 1;

# 方法 2.
# Write your MySQL query statement below
SELECT
    t.person_name
FROM (
    SELECT
        turn,
        person_name,
        weight,
        SUM(weight) OVER (ORDER BY turn) AS cum_sum
    FROM Queue
) t
WHERE t.cum_sum <= 1000
ORDER BY turn DESC
LIMIT 1;
