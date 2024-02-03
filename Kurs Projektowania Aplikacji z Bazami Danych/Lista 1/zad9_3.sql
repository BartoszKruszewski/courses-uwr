UPDATE SalesLT.SalesOrderHeader
SET  CreditCardApprovalCode = 'x'
WHERE SalesOrderID IN (
    SELECT SalesOrderID
    FROM SalesLT.SalesOrderHeader AS s
    JOIN SalesLT.Customer AS c ON c.CustomerID = s.CustomerID
    WHERE s.CreditCardApprovalCode = 42
)
