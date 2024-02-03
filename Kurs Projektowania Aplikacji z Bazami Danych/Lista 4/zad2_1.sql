drop table if exists SalesLT.ProductPriceHistory;
go

create table SalesLT.ProductPriceHistory (
    ProductPriceHistoryID int primary key identity,
    ProductID int,
    StandardCost money,
    ListPrice money,
    ChangeDate datetime
);
go

drop trigger if exists SalesLT.tgr_ProductPriceHistory;
go

create trigger tgr_ProductPriceHistory
on SalesLT.Product
after update
as
begin
    if update(StandardCost) or update(ListPrice)
    begin
        insert into SalesLT.ProductPriceHistory (ProductID, StandardCost, ListPrice, ChangeDate)
        select 
            inserted.ProductID,
            coalesce(inserted.StandardCost, deleted.StandardCost),
            coalesce(inserted.ListPrice, deleted.ListPrice),
            getdate()
        from inserted
        inner join deleted on inserted.ProductID = deleted.ProductID;
    end
end;
go

drop trigger if exists SalesLT.tgr_ProductDeletion;
go

create trigger tgr_ProductDeletion
on SalesLT.Product
after delete
as
begin
    insert into SalesLT.ProductPriceHistory (ProductID, StandardCost, ListPrice, ChangeDate)
    select ProductID, StandardCost, ListPrice, getdate()
    from deleted;
end;
go