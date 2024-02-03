delete from SalesLT.Product
where Name = 'some product';
go

insert into SalesLT.Product (Name, StandardCost, ListPrice, ProductNumber, SellStartDate)
values ('some product', 50.00, 100.00, 1, getdate());
go

update SalesLT.Product
set StandardCost = 55.00
where Name = 'some product';
go

update SalesLT.Product
set ListPrice = 110.00
where Name = 'some product';
go

delete from SalesLT.Product
where Name = 'some product';
go

select *
from SalesLT.ProductPriceHistory;
go




