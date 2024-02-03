DROP PROCEDURE IF EXISTS AllDays
GO

DROP TYPE IF EXISTS ReaderIDTableType
GO

CREATE TYPE ReaderIDTableType AS TABLE (ReaderID INT);
GO

CREATE PROCEDURE AllDays (@ReaderIDs ReaderIDTableType READONLY)
AS
BEGIN
    CREATE TABLE #TotalDays (
        ReaderID INT,
        SumDays INT
    )

    INSERT INTO #TotalDays (ReaderID, SumDays)
    SELECT
        w.Czytelnik_ID,
        SUM(w.Liczba_Dni) AS SumDays
    FROM
        Wypozyczenie AS w
    WHERE
        w.Czytelnik_ID IN (SELECT ReaderID FROM @ReaderIDs)
    GROUP BY
        w.Czytelnik_ID

    SELECT * FROM #TotalDays

    DROP TABLE #TotalDays
END;
GO

DECLARE @readers_id AS ReaderIDTableType

INSERT INTO @readers_id (ReaderID)
VALUES (1), (2), (3)

EXEC AllDays @ReaderIDs = @readers_id;
GO

