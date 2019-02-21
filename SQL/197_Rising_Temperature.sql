SELECT w1.Id
FROM Weather AS w1
JOIN Weather AS w2
ON DATEDIFF(w1.RecordDate, w2.RecordDate) = 1
WHERE w1.Temperature > w2.Temperature
