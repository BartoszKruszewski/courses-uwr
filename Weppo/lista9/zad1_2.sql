drop table if exists OSOBA;
create table OSOBA (
    ID int identity(1,1) primary key,
    IMIE varchar(50),
    NAZWISKO varchar(50),
    PLEC varchar(1)
);

insert into OSOBA (IMIE, NAZWISKO, PLEC) 
values ('Jan', 'Kowalski', 'M');
insert into OSOBA (IMIE, NAZWISKO, PLEC) 
values ('Anna', 'Nowak', 'K');

select * from OSOBA;
