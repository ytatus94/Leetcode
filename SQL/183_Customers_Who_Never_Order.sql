SELECT Customers.Name AS Customers
FROM Customers
LEFT JOIN Orders
ON Customers.Id = Orders.CustomerID
WHERE Orders.CustomerID IS NULL;


-- 另一個寫法
SELECT name AS Customers
FROM Customers AS c
LEFT JOIN Orders AS o
ON c.id = o.customerId
WHERE o.customerId IS NULL
