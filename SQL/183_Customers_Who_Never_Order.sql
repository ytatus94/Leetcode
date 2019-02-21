SELECT Customers.Name AS Customers FROM Customers
LEFT JOIN Orders
ON Customers.Id = Orders.CustomerID
WHERE Orders.CustomerID IS NULL;
