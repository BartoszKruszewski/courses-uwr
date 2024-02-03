DROP TABLE IF EXISTS ProductDescription_Backup_Cursor;
GO

CREATE TABLE ProductDescription_Backup_Cursor (
    ProductDescriptionID INT PRIMARY KEY,
    Description NVARCHAR(400),
    rowguid UNIQUEIDENTIFIER,
    ModifiedDate DATETIME,
);

DECLARE @ProductDescriptionID INT;
DECLARE @Description NVARCHAR(400);
DECLARE @rowguid UNIQUEIDENTIFIER;
DECLARE @ModifiedDate DATETIME;

DECLARE productDescriptionCursor CURSOR FOR
SELECT * FROM SalesLT.ProductDescription;

OPEN productDescriptionCursor;

FETCH NEXT FROM productDescriptionCursor 
INTO @ProductDescriptionID, @Description, @rowguid, @ModifiedDate;

WHILE @@FETCH_STATUS = 0
BEGIN
    INSERT INTO ProductDescription_Backup_Cursor (
        ProductDescriptionID, 
        Description,
        rowguid,
        ModifiedDate
    )
    VALUES (
        @ProductDescriptionID,
        @Description,
        @rowguid,
        @ModifiedDate
    );

    FETCH NEXT FROM productDescriptionCursor
    INTO @ProductDescriptionID, @Description, @rowguid, @ModifiedDate;
END;

CLOSE productDescriptionCursor;
DEALLOCATE productDescriptionCursor;
GO
