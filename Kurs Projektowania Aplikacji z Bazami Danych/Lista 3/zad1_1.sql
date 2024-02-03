DROP TABLE IF EXISTS ProductDescription_Backup;
GO

SELECT *
INTO ProductDescription_Backup
FROM SalesLT.ProductDescription;
GO