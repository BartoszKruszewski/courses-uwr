DROP PROCEDURE IF EXISTS GenerateRandomPairs
GO

CREATE PROCEDURE GenerateRandomPairs(@n INT) AS
BEGIN
    DELETE FROM fldata;
    
    DECLARE @cartesian TABLE (
        firstname VARCHAR(255),
        lastname VARCHAR(255)
    );

    INSERT INTO @cartesian (firstname, lastname)
        SELECT firstname, lastname
        FROM firstnames
        CROSS JOIN lastnames;

    DECLARE @possible_pairs INT;
    SELECT @possible_pairs = COUNT(*)
    FROM @cartesian;

    IF @n > @possible_pairs
        THROW 50000, 'n cannot be that big!', 1;

    INSERT INTO fldata (firstname, lastname)
        SELECT TOP(@n) firstname, lastname
        FROM @cartesian
        ORDER BY NEWID()
END;
GO

EXEC GenerateRandomPairs @n = 5;
GO

SELECT * FROM fldata;
GO
