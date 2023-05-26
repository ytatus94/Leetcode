SELECT MIN(ABS(p1.x - p2.x)) AS shortest
FROM point AS p1
JOIN point AS p2
WHERE p1.x != p2.x
