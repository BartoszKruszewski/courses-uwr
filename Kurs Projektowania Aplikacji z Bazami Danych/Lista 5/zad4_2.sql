begin tran
insert liczby2 values (1)
waitfor delay '00:00:10'
update liczby1 set liczba = 10

SELECT * FROM sys.sysprocesses