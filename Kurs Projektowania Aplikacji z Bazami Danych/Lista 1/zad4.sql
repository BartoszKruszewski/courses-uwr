SELECT
    DISTINCT pc1.[Name] as [Catergory Name],
    p.[Name] as [Product Name]
FROM
    SalesLT.ProductCategory AS pc1
    JOIN SalesLT.ProductCategory AS pc2 ON pc1.ProductCategoryID = pc2.ParentProductCategoryID
    JOIN SalesLT.Product AS p ON p.ProductCategoryID = pc1.ProductCategoryID