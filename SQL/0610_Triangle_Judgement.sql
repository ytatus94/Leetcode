-- 三角形的兩邊之和要大於第三邊
SELECT
    x, y, z, 
    CASE
        WHEN x+y > z AND y+z > x AND x+z > y THEN 'Yes'
        ELSE 'No'
    END AS 'triangle'
FROM triangle;
