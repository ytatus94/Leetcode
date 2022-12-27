SELECT w1.Id
FROM Weather AS w1
JOIN Weather AS w2
ON DATEDIFF(w1.RecordDate, w2.RecordDate) = 1
WHERE w1.Temperature > w2.Temperature

-- 方法 2
SELECT w2.id AS id
FROM Weather w1, Weather w2
WHERE DATEDIFF(w2.recordDate, w1.recordDate) = 1
AND w2.temperature > w1.temperature 
