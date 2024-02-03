SELECT 
    pm.Name, 
    COUNT(ProductID) AS [Number of Products]
FROM 
    SalesLT.Product as p
    JOIN SalesLT.ProductModel as pm ON p.ProductModelID = pm.ProductModelID
GROUP BY pm.Name
HAVING COUNT(ProductID) > 1