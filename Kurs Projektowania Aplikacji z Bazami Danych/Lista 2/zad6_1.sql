DROP TABLE IF EXISTS #LocalTempTable
GO

DROP TABLE IF EXISTS ##GlobalTempTable
GO

DECLARE @TableVariable TABLE (ID INT, Name NVARCHAR(50));
INSERT INTO @TableVariable VALUES (1, 'Alice');

CREATE TABLE #LocalTempTable (ID INT, Name NVARCHAR(50));
INSERT INTO #LocalTempTable VALUES (2, 'Bob');

CREATE TABLE ##GlobalTempTable (ID INT, Name NVARCHAR(50));
INSERT INTO ##GlobalTempTable VALUES (3, 'Charlie');

SELECT * FROM @TableVariable;     
SELECT * FROM #LocalTempTable;     
SELECT * FROM ##GlobalTempTable;  

SELECT TABLE_NAME
FROM tempdb.INFORMATION_SCHEMA.tables
GO