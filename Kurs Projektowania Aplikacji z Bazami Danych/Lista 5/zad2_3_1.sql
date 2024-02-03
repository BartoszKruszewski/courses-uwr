delete from dbo.Products where ID = 5;

begin transaction;
    set transaction isolation level read uncommitted;
    select * from dbo.Products;
    waitfor delay '00:00:05'
    select * from dbo.Products;
commit transaction;