
DROP TABLE IF EXISTS Prices;
GO

DROP TABLE IF EXISTS Rates;
GO

DROP TABLE IF EXISTS Products;
GO

CREATE TABLE Products (
    ID INT PRIMARY KEY,
    ProductName NVARCHAR(255)
);
GO

CREATE TABLE Rates (
    Currency NVARCHAR(50) PRIMARY KEY,
    PricePLN DECIMAL(18, 2)
);
GO

CREATE TABLE Prices (
    ProductID INT,
    Currency NVARCHAR(50),
    Price DECIMAL(18, 2),
    FOREIGN KEY (ProductID) REFERENCES Products(ID)
);
GO

INSERT INTO Products (ID, ProductName) VALUES (1, 'Shoes');
INSERT INTO Products (ID, ProductName) VALUES (2, 'Shirt');
INSERT INTO Products (ID, ProductName) VALUES (3, 'Jacket');
INSERT INTO Products (ID, ProductName) VALUES (4, 'Cap');

INSERT INTO Rates (Currency, PricePLN) VALUES ('USD', 4.22);
INSERT INTO Rates (Currency, PricePLN) VALUES ('EUR', 4.47);
INSERT INTO Rates (Currency, PricePLN) VALUES ('GBP', 5.12);

INSERT INTO Prices (ProductID, Currency, Price) VALUES (1, 'USD', 200.00);
INSERT INTO Prices (ProductID, Currency, Price) VALUES (2, 'EUR', 100.00);
INSERT INTO Prices (ProductID, Currency, Price) VALUES (3, 'PLN', 300.00);
INSERT INTO Prices (ProductID, Currency, Price) VALUES (4, 'GBP', 50.00);
GO

DECLARE @ProductID INT
DECLARE @Currency NVARCHAR(50)
DECLARE @Price DECIMAL(18, 2)

-- wyznaczanie kursora z wierszami, ktorych nie ma w Rates 
DECLARE PriceCursor CURSOR FOR
SELECT p.ProductID, p.Currency
FROM Prices p
LEFT JOIN Rates r ON p.Currency = r.Currency
WHERE r.Currency IS NULL

OPEN PriceCursor
FETCH NEXT FROM PriceCursor INTO @ProductID, @Currency

WHILE @@FETCH_STATUS = 0
BEGIN
    -- usuwanie wierszy z kursora z tabeli Prices
    DELETE FROM Prices
    WHERE ProductID = @ProductID AND Currency = @Currency

    FETCH NEXT FROM PriceCursor INTO @ProductID, @Currency
END

CLOSE PriceCursor
DEALLOCATE PriceCursor

-- przeliczenie cen na podstawie Rates
UPDATE p
SET Price = r.PricePLN * p.Price
FROM Prices p
JOIN Rates r ON p.Currency = r.Currency

SELECT * FROM Prices;