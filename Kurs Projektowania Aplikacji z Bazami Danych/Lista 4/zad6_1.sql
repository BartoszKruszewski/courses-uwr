drop table if exists Cache;
go

create table Cache (
    ID int identity primary key,
    UrlAddress varchar(255) not null,
    LastAccess datetime not null
);
go

drop table if exists History;
go

create table History (
    ID int identity primary key,
    UrlAddress varchar(255) not null,
    LastAccess datetime not null
);
go

drop table if exists Parameters;
go


create table Parameters (
    Name varchar(50) primary key,
    Value int not null
);
go

insert into Parameters (Name, Value)
values ('max_cache', 3);
go

drop trigger if exists trg_insert_cache;
go

create trigger trg_insert_cache
on Cache
instead of insert
as
begin
    declare @cache_size int;
    declare @max_cache_size int;
    declare @inserted_url varchar(255);
    declare @inserted_date date;

    select @cache_size = count(*) from Cache;
    select @max_cache_size = Value from Parameters where Name = 'max_cache';
    select @inserted_url = UrlAddress from inserted;
    select @inserted_date = LastAccess from inserted;
    
    if exists (select top 1 * from Cache where UrlAddress = @inserted_url) 
    begin
        update Cache 
        set LastAccess = @inserted_date
        where UrlAddress = @inserted_url
    end
    else
    begin
        if @cache_size < @max_cache_size 
        begin
            insert into Cache (UrlAddress, LastAccess)
            select UrlAddress, LastAccess
            from inserted
        end
        else
        begin
            declare @oldest_access_time datetime;

            select @oldest_access_time = min(LastAccess) 
            from Cache;

            insert into History (UrlAddress, LastAccess)
            select UrlAddress, LastAccess 
            from Cache 
            where LastAccess = @oldest_access_time;

            update Cache
            set UrlAddress = @inserted_url, LastAccess = @inserted_date
            where LastAccess = @oldest_access_time;
        end
    end
end;
go

drop trigger if exists trg_insert_history;
go

create trigger trg_insert_history
on History
instead of insert
as
begin
    declare @inserted_url varchar(255);
    declare @inserted_date date;
    select @inserted_url = UrlAddress from inserted;
    select @inserted_date = LastAccess from inserted;

    if exists (select top 1 * from History where UrlAddress = @inserted_url) 
    begin
        update History
        set LastAccess = @inserted_date
        where UrlAddress = @inserted_url
    end
    else
    begin
        insert into History (UrlAddress, LastAccess)
        values (@inserted_url, @inserted_date)
    end
end;
go

insert into Cache (UrlAddress, LastAccess)
values ('www.google.com', '2023-10-24');
go

insert into Cache (UrlAddress, LastAccess)
values ('www.google.com', '2023-10-25');
go

insert into Cache (UrlAddress, LastAccess)
values ('www.youtube.com', '2023-11-01');
go

insert into Cache (UrlAddress, LastAccess)
values ('www.instagram.com', '2023-11-03');
go

insert into Cache (UrlAddress, LastAccess)
values ('www.facebook.com', '2023-11-04');
go

select * from Cache;
select * from History;