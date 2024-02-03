drop table if exists liczby1;
drop table if exists liczby2;
create table liczby1 (liczba int)
create table liczby2 (liczba int)
go

-- set transaction isolation level read uncommitted;
-- set transaction isolation level read committed;
-- set transaction isolation level repeatable read;
-- set transaction isolation level snapshot;
set transaction isolation level serializable;
begin tran
    insert liczby1 values (1)
    waitfor delay '00:00:10'
    update liczby2 set liczba = 10
    waitfor delay '00:00:10'