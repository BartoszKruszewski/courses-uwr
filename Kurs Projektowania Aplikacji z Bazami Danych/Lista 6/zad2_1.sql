set showplan_all on;
go

select distinct c.PESEL, c.Nazwisko
from Egzemplarz e
join Ksiazka k on e.Ksiazka_ID = k.Ksiazka_ID
join Wypozyczenie w on e.Egzemplarz_ID = w.Egzemplarz_ID
join Czytelnik c on c.Czytelnik_ID = w.Czytelnik_ID;
go

select c.PESEL, c.Nazwisko
from Czytelnik c 
where c.Czytelnik_ID in
    (select w.Czytelnik_ID 
    from Wypozyczenie w
    join Egzemplarz e on e.Egzemplarz_ID = w.Egzemplarz_ID
    join Ksiazka k on e.Ksiazka_id = k.Ksiazka_ID);
go

select c.PESEL, c.Nazwisko
from Czytelnik c 
where c.Czytelnik_ID in
    (select w.Czytelnik_ID 
    from Wypozyczenie w
    where w.Egzemplarz_ID in
        (select e.Egzemplarz_ID
        from Egzemplarz e
        join Ksiazka k on e.Ksiazka_id = k.Ksiazka_ID));
go

set showplan_all off;
go
