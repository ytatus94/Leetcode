SELECT ROUND(SQRT(MIN(POWER(p1.x-p2.x, 2) + POWER(p1.y-p2.y, 2))), 2) AS shortest
FROM point_2d AS p1
JOIN point_2d AS p2
ON p1.x != p2.y OR p1.y != p2.y
