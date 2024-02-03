drop table if exists OSOBA;
create table OSOBA (
    ID int primary key,
    IMIE varchar(50),
    NAZWISKO varchar(50),
    PLEC varchar(1)
);

drop sequence if exists OSOBA_SEQ;
create sequence OSOBA_SEQ
    as int
    start with 1
    increment by 1
    minvalue 1;

insert into OSOBA (ID, IMIE, NAZWISKO, PLEC) 
values (next value for OSOBA_SEQ, 'Jan', 'Kowalski', 'M');
insert into OSOBA (ID, IMIE, NAZWISKO, PLEC) 
values (next value for OSOBA_SEQ, 'Anna', 'Nowak', 'K');

select * from OSOBA;
