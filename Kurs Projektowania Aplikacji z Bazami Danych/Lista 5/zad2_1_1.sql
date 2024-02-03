begin transaction;
    update dbo.Products set ProductName = 'dirty' where ID = 1;
    waitfor delay '00:00:10'
rollback transaction;

