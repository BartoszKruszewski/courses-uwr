DROP FUNCTION IF EXISTS GetReadersWithSpecimens
GO

CREATE FUNCTION GetReadersWithSpecimens(@MinDaysHeld INT)
RETURNS @ResultTable TABLE (PESEL VARCHAR(11), SpecimensCount INT)
AS
BEGIN
    INSERT INTO @ResultTable (PESEL, SpecimensCount)
    SELECT
        c.PESEL,
        COUNT(w.Wypozyczenie_ID) AS SpecimensCount
    FROM Czytelnik AS c
    JOIN Wypozyczenie AS w ON c.Czytelnik_ID = w.Czytelnik_ID
    WHERE w.Liczba_Dni >= @MinDaysHeld
    GROUP BY c.PESEL

    RETURN
END;
GO

SELECT * FROM GetReadersWithSpecimens(10);
GO