SELECT
    City,
    COUNT(DISTINCT c.CustomerID) AS Customers,
    COUNT(DISTINCT c.SalesPerson) AS [Sales Persons]
FROM
    SalesLT.Customer AS c
    JOIN SalesLT.CustomerAddress AS ca ON c.CustomerID = ca.CustomerID
    JOIN SalesLT.Address AS a ON ca.AddressID = a.AddressID
GROUP By City
