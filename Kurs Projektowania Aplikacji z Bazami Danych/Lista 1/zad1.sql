SELECT 
    City AS Cities
FROM 
    SalesLT.Address AS a
    JOIN SalesLT.SalesOrderHeader AS s ON a.AddressID = s.ShipToAddressID
