drop table if exists MIEJSCE_PRACY;
create table MIEJSCE_PRACY (
    ID int primary key IDENTITY(1,1),
    NAZWA varchar(100) not null
);

drop table if exists OSOBA;
create table OSOBA (
    ID int primary key IDENTITY(1,1),
    IMIE varchar(50) not null,
    NAZWISKO varchar(50) not null,
    ID_MIEJSCE_PRACY int foreign key references MIEJSCE_PRACY(ID)
);