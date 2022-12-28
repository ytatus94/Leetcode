-- 考會不會 join
SELECT Customers.Name AS Customers
FROM Customers
LEFT JOIN Orders
ON Customers.Id = Orders.CustomerID
WHERE Orders.CustomerID IS NULL;


-- 用 alias 的寫法
SELECT name AS Customers
FROM Customers AS c
LEFT JOIN Orders AS o
ON c.id = o.customerId
WHERE o.customerId IS NULL;
