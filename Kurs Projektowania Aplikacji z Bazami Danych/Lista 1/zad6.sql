SELECT
    c.FirstName,
    c.LastName,
    SUM(UnitPriceDiscount * UnitPrice)
FROM
    SalesLT.Customer as c
    JOIN SalesLT.SalesOrderHeader as oh ON c.CustomerID = oh.CustomerID
    JOIN SalesLT.SalesOrderDetail as od ON oh.SalesOrderID = od.SalesOrderID
GROUP BY c.CustomerID, c.FirstName, c.LastName
