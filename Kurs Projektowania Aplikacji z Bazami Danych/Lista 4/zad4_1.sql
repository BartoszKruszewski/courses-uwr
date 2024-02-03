drop trigger if exists trg_max_5_specimen;
go

create trigger trg_max_5_specimen
on Egzemplarz
instead of insert
as
begin
    declare @book_id int;
    select @book_id = Ksiazka_ID
    from inserted

    declare @specimen_count int;

    select @specimen_count = count(*)
    from Egzemplarz
    where Ksiazka_ID = @book_id;

    print(@specimen_count);

    if @specimen_count >= 5
    begin

        raiserror('A book can have a maximum of 5 specimens.', 16, 1);
        rollback;
    end
    else
    begin
        insert into Egzemplarz (Sygnatura, Ksiazka_ID)
        select Sygnatura, Ksiazka_ID
        from inserted;
    end
end;
go

alter table Egzemplarz enable trigger trg_max_5_specimen;

delete from Egzemplarz
where Ksiazka_ID = 1;
go

insert into Egzemplarz (Sygnatura, Ksiazka_ID)
values ('S0101', 1);
go

insert into Egzemplarz (Sygnatura, Ksiazka_ID)
values ('S0102', 1);
go

insert into Egzemplarz (Sygnatura, Ksiazka_ID)
values ('S0103', 1);
go

insert into Egzemplarz (Sygnatura, Ksiazka_ID)
values ('S0104', 1);
go

insert into Egzemplarz (Sygnatura, Ksiazka_ID)
values ('S0105', 1);
go

insert into Egzemplarz (Sygnatura, Ksiazka_ID)
values ('S0106', 1);
go

select * from Egzemplarz;
go
