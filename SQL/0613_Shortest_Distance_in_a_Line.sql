-- 直線上的兩個點的最短距離，就用 |x1 - x2|
-- 這題就是考會不會用 ABS()
-- 注意這題要找出所有距離中最小值，所以要有 MIN()
SELECT MIN(ABS(p1.x - p2.x)) AS shortest
FROM point AS p1
JOIN point AS p2
WHERE p1.x != p2.x;
