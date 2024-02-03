drop table if exists SalesLT.brand_approvals;
go

create table SalesLT.brand_approvals(
    brand_id int identity primary key,
    brand_name varchar(255) not null
);
go

drop table if exists SalesLT.brands;
go

create table SalesLT.brands(
    brand_id int identity primary key,
    brand_name varchar(255) not null
);
go

drop view if exists SalesLT.vw_brands;
go

create view SalesLT.vw_brands 
as
select
    brand_name,
    'Approved' approval_status
from
    SalesLT.brands
union
select
    brand_name,
    'Pending Approval' approval_status
from
    SalesLT.brand_approvals;
go

drop trigger if exists SalesLT.trg_vw_brands;
go

create trigger SalesLT.trg_vw_brands 
on SalesLT.vw_brands
instead of insert
as
begin
    set nocount on;
    insert into SalesLT.brand_approvals ( 
        brand_name
    )
    select
        i.brand_name
    from
        inserted i
    where
        i.brand_name not in (
            select 
                brand_name
            from
                SalesLT.brands
        );
end
go
