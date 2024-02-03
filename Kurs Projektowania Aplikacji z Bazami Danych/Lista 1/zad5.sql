SELECT TOP(5)
    h.SalesOrderID,
    SalesOrderNumber,
    PurchaseOrderNumber,
    SUM(UnitPrice) AS [Total Sum],
    SUM(UnitPrice * UnitPriceDiscount) AS [Total Discount],
    SUM(UnitPrice * (1 - UnitPriceDiscount)) AS [Total Sum With Discount]
FROM
    SalesLT.SalesOrderHeader AS h
    JOIN SalesLT.SalesOrderDetail AS d ON h.SalesOrderID = d.SalesOrderID
GROUP BY h.SalesOrderID, SalesOrderNumber, PurchaseOrderNumber
ORDER BY [Total Discount] DESC

