-- 兩點之間的最短距離就是直線
-- distance = sqrt( (x1 - x2)^2 + (y1 - y2)^2 )
-- 這一題就是考會不會用 POWER(), SQRT() 等函數
-- 還有要找的是全部的點裡面的最短距離，所以要記得加上 MIN()
SELECT ROUND(SQRT(MIN(POWER(p1.x-p2.x, 2) + POWER(p1.y-p2.y, 2))), 2) AS shortest
FROM point_2d AS p1
JOIN point_2d AS p2
ON p1.x != p2.x OR p1.y != p2.y;
