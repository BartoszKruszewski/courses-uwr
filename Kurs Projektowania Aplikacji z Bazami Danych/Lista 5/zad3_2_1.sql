drop table if exists liczby;
go

create table liczby ( liczba int );
go

insert liczby values ( 10 );
go

set transaction isolation level serializable;

insert liczby values ( 10 );

begin transaction

    waitfor delay '00:00:05'
    select resource_type, request_mode, request_status from sys.dm_tran_locks;

    select * from liczby

    waitfor delay '00:00:05'
    select resource_type, request_mode, request_status from sys.dm_tran_locks;

commit