SELECT product_id,
       "store1" AS store,
       CASE
           WHEN store1 THEN store1
       END AS price
FROM Products
WHERE store1 IS NOT NULL
UNION
SELECT product_id,
       "store2" AS store,
       CASE
           WHEN store2 THEN store2
       END AS price
FROM Products
WHERE store2 IS NOT NULL
UNION
SELECT product_id,
       "store3" AS store,
       CASE
           WHEN store3 THEN store3
       END AS price
FROM Products
WHERE store3 IS NOT NULL
