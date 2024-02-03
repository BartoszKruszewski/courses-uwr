update SalesLT.Customer
set FirstName = 'Bartek'
where CustomerID = 5;
go

select FirstName, ModifiedDate 
from SalesLT.Customer
where CustomerID = 5;
go
