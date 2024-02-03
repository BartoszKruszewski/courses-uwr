set nocount on

-- wypelnienie tabeli liczba od 1 do 60
drop table if exists liczby
go
create table liczby( nr int primary key, liczba int )
go
declare @a int
set @a=1
while ( @a<=60)
begin
    insert liczby values ( @a, @a )
    set @a=@a+1
end
go

-- deklaracja zmiennej x = 10
declare @x int
set @x=10

-- Dynamic: na bierząco pobiera dane z tabeli
--declare c cursor dynamic for select liczba from liczby where liczba<=@x
-- Static: pobiera dane z tabeli raz podczas utworzenia go
--declare c cursor static for select liczba from liczby where liczba<=@x
-- Keyset: pobiera klucze z tabeli raz poczas utworzenia go i dynamicznie pobiera wartości
declare c cursor keyset for select liczba from liczby where liczba<=@x

set @x=20

open c


declare @aux int, @licznik int
set @licznik=2

print 'Kolejne liczby z kursora:'
fetch next from c into @aux 
while ( @@fetch_status=0 )
begin
    print 'Liczba: '+cast(@aux as varchar)
    print 'Licznik: '+cast(@licznik as varchar)
    -- usuwanie wierszy z tabeli, dla dynamic i keyset zmniejsza ilosc danych
    delete from liczby where liczba=@licznik
    fetch next from c into @aux 
    set @licznik=@licznik+2
end

-- dla keyset fetch jest rowny -2 czyli blad bo pamieta klucz dla ktorego zostala usunieta wartosc
print 'Status ostatniej instrukcji fetch: ' + cast(@@fetch_status as varchar)

close c
deallocate c

select * from liczby where liczba<=10