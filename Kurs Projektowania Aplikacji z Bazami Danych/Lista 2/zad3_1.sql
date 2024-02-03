DROP PROCEDURE IF EXISTS AddReader
GO

CREATE PROCEDURE AddReader ( 
    @pesel NVARCHAR(11),
    @lastname NVARCHAR(50),
    @birth_date DATE
) 
AS
BEGIN
    IF LEN(@pesel) != 11 OR @pesel NOT LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
        THROW 51000, 'Invalid PESEL format!', 1;

    IF LEN(@lastname) < 2 
        THROW 51001, 'Lastname should have at least 2 letters!', 1;

    IF NOT ASCII(LEFT(@lastname, 1)) BETWEEN 65 AND 90
        THROW 51002, 'Lastname should start from capital letter!', 1;
    
    IF @birth_date IS NULL OR @birth_date > GETDATE()
        THROW 51003, 'Wrong birth date!', 1;

    INSERT INTO Czytelnik (
        PESEL, Nazwisko, Data_Urodzenia
    ) 
    VALUES (
        @pesel, 
        @lastname, 
        @birth_date
    );
END;
GO

EXEC AddReader 
    @pesel = '12345678918',
    @lastname = 'Kruszewski',
    @birth_date = '2003-10-24';
GO