UPDATE SalesLT.SalesOrderHeader
SET  CreditCardApprovalCode = 42
WHERE SalesOrderID IN (
    SELECT TOP(3) SalesOrderID
    FROM SalesLT.SalesOrderHeader
    ORDER BY RAND()
)