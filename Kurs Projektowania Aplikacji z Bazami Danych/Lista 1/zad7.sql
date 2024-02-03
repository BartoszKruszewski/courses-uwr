CREATE TABLE Test (
   ID INT IDENTITY(1000, 10) PRIMARY KEY,
   Field VARCHAR(255)
)



-- @@IDENTITY zwraca ostatnia wartosc identity dodana do jakiejkolwiek tabeli

-- IDENT_CURRENT() wymaga podania,
-- z jakiej tabeli ma pochodzic wartosc identity, ktora ma zwrocic