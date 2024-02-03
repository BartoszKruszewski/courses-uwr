drop trigger if exists SalesLT.trg_UpdateModifiedDate;
go

create trigger trg_UpdateModifiedDate
on saleslt.customer
after update
as
begin
    update saleslt.customer
    set modifieddate = getdate()
    from inserted
    where saleslt.customer.customerid = inserted.customerid;
end;

go
