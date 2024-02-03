DROP PROCEDURE IF EXISTS SetDiscontinuedDates
GO

DROP TYPE IF EXISTS ProductSetDatesTableType
GO

CREATE TYPE ProductSetDatesTableType AS TABLE (ProductID INT);
GO

CREATE PROCEDURE SetDiscontinuedDates (
    @product_set_dates ProductSetDatesTableType READONLY,
    @discontinued_date DATE
)
AS
BEGIN
    UPDATE SalesLT.Product
    SET DiscontinuedDate = @discontinued_date
    WHERE 
        ProductID IN (SELECT ProductID FROM @product_set_dates)
        AND DiscontinuedDate IS NULL
END;
GO

DECLARE @product_set_dates AS ProductSetDatesTableType

INSERT INTO @product_set_dates (ProductID)
VALUES (680), (720), (714)

EXEC SetDiscontinuedDates 
    @product_set_dates = @product_set_dates,
    @discontinued_date = '2023-10-24';
GO

SELECT ProductID, DiscontinuedDate FROM SalesLT.Product
GO

