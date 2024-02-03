update dbo.Products set ProductName = 'clean' where ID = 1;

begin transaction;
    set transaction isolation level read uncommitted;
    select ProductName from dbo.Products where ID = 1;
    waitfor delay '00:00:05'
    select ProductName from dbo.Products where ID = 1;
commit transaction;

