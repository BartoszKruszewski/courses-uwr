1.

Instalacja IIS:
	- panel sterowania -> programy -> włącz lub wyłącz funkcje systemu windows -> internetowe usługi informacyjne ->
	  usługi WWW -> funkcje tworzenia aplikacji
	- zaznaczenie wszystkich opcji
	- kliknięcie ok, wtedy system zaczyna je instalować
Sprawdzenie statusu ASP.NET:
	- uruchomienie IIS
	- zaznaczenie lokalnego serwera
	- wybór ograniczenia ISAPI i CGI
	- sprawdzenie na liście czy ASP.NET ma status "Dozwolone"

2.

Dodanie witryny:
	- uruchomienie IIS menagera
	- kliknięcie prawym na "witryny" i wybranie dodaj witrynę sieci web
	- uzupełnienie danych witryny (w ścieżce podać w jakim katalogu na dysku będzie się znajdować witryna:
	  C:/inetpub/ap1; adres ip podać jako 127.0.0.1, a nazwę hosta jako ap1.myserver.com)
Podłączenie hosta w systemie:
	- otworzyć plik C:/Windows/System32/Drivers/etc/hosts jako administator i podpisać na końcu pliku:
	  127.0.0.1 ap1.myserver.com
Utworzenie zawartości serwera:
	- utworzyć folder C:/inetpub/ap1
	- dodać do niego plik index.html z jaką przykładową zawartością
	- wejść we właściwości folderu C:/inetpub/ap1 -> zabezpieczenia -> edytuj -> dodaj
	- podać nazwę nowego użytkownika jako "IIS AppPool\ap1"
Otworzyć w przeglądarce link http://ap1.myserver.com

3.

Dodawanie drugiego nagłówka hostu:
	- IIS menager -> witryna którą chcemy podłączyć pod drugiego hosta (ap1) -> dodaj powiązania -> dodaj
	- uzupełnienie danych podłączenia (adres ip podać jako 127.0.0.1, a nazwę hosta jako ap2.myserver.com)
	- otworzyć plik C:/Windows/System32/Drivers/etc/hosts jako administator i podpisać na końcu pliku:
	  127.0.0.1 ap2.myserver.com

Otworzyć w przeglądarce link http://ap1.myserver.com
Otworzyć w przeglądarce link http://ap2.myserver.com

Powinny prowadzić do tej samej strony

Zastosowania:
	- różne subdomeny, taki sam zestaw plików
	- podłączenie wielu wykupionych domen do jednej witryny
	- testy przy zmianie nazwy domeny
	- korzystanie z nagłówków hostów w logice aplikacji (np. identyfikacja grup użytkowników)

4.

Udostępnianie pliku z rozszerzeniem .foo w witrynie:
	- umieść w folderze C:/inetpub/ap1 przykładowy plik example.foo
	- IIS meneger -> witryna pod którą podpinamy plik -> typy MIME -> dodaj
	- ustaw rozszerzenie na .foo a typ MIME na application/octet-stream

Otworzyć w przeglądarce link http://ap1.myserver.com/example.foo

Plik example.foo powinien zostać pobrany

5.

Utworzenie projektu:
	- w instalerze do Visual Studio wybieramy modyfikuj i wybieramy wszystkie opcje do ASP.NET i .NET
	- instalujemy to
	- tworzymy nowe solution w Visual Studio
	- klikamy prawym na solution -> add -> new project
	- wybieramy ASP.NET web application (.NET Framework)
	- wyłączamy opcje configure for HTTPS
	- wybieramy projekt Empty
	- dodajemy plik WebForm1.aspx i dodajemy do niego cokolwiek

Uruchamiamy projekt na IIS Express zieloną strzałką, mając zaznaczony plik WebForm1.aspx
Powinniśmy zostać przekierowani do przeglądarki na stronę localhost:JAKIS_PORT/WebForm1.aspx

Publikowanie aplikacji na IIS:
	- tworzymy folder C:/temp/NAZWA_FOLDERU
	- klikamy prawym na projekt i wybieramy opcje Publish
	- wybieramy foler i podajemy ścieżkę C:/temp/NAZWA_FOLDERU
	- klikamy publish (nasze projekt zostanie wykesportowany do C:/temp/NAZWA_FOLDERU)
	- tworzymy nową witrynę jak w poprzednich zadaniach i dodajemy do jej folderu pliki

Otwieramy http://NASZ_HOST/WebForm1.aspx
Powinniśmy uzyskać taka sama strone jak przy uruchomieniu IIS Express

6.

Utworzenie projektu:
	- otwieamy Visual Studio
	- klikamy prawym na solution -> add -> new project
	- wybieramy ASP.NET Core Empty
	- wyłączamy opcje configure for HTTPS
	- dodajemy plik WebForm1.aspx i dodajemy do niego cokolwiek
	- w pliku Program.cs dodajemy jakiś przykładowy endpoint

Uruchamiamy projekt na IIS Express zieloną strzałką
Powinniśmy zostać przekierowani do przeglądarki na stronę localhost:JAKIS_PORT

Publikujemy tak samo jak w zadaniu 5.

Otwieramy http://ap1.myserver.com
Powinniśmy uzyskać taka sama strone jak przy uruchomieniu IIS Express

7.

dodajmy do WebForm1.aspx:

<form id="form1" runat="server">
    <div>
        <asp:TextBox ID="txtName" runat="server" Placeholder="Wpisz swoje imię"></asp:TextBox>
        <asp:Button ID="btnSubmit" runat="server" Text="Wyślij" OnClick="btnSubmit_Click" />
    </div>
</form>

dodajmy do WebForm1.aspx.cs:

protected void btnSubmit_Click(object sender, EventArgs e)
{
    string userName = txtName.Text;
    System.Diagnostics.Debug.WriteLine("Imię użytkownika: " + userName);
}

Uruchamiamy projekt na IIS Express zieloną strzałką, mając zaznaczony plik WebForm1.aspx
Powinniśmy zostać przekierowani do przeglądarki na stronę localhost:JAKIS_PORT/WebForm1.aspx
Wyniki z formularza powinny wyświetlać się w okienku output.

8.

Tworzymy dwóch nowych użytkoników lokalnych (nie administratorów) w systemie (muszą mieć ustawione jakieś hasło).

Do naszej aplikacji .NET CORE dodajemy następujący kod:

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => {
    string filePath = @"C:\temp\example.txt";
    string fileContent;

    try
    {
        using StreamReader sr = new StreamReader(filePath);
        fileContent = sr.ReadToEnd();
    }
    catch (Exception ex)
    {
        fileContent = ex.Message;
    }

    return Results.Text(fileContent);
});

app.Run();

Tworzymy plik C:\temp\example.txt z jakąś przykładową zawartością:
	- wchodzimy w jego właściwości -> zabepieczenia -> zaawansowane -> wyłącz dziedziczenie -> usuń pozwolenia
	- następnie dajemy edytuj -> dodaj
	- podajemy nazwę naszego pierwszego nowoutworzonego użytkownika lokalnego

W IIS menagarze ustawimy tworzymy nową witrynę a następnie publikujmey do jej folderu naszą aplikację z Visual Studio.

Pokazujemy, że po otwarciu strony w przeglądarce, dostajemy odmowę dostępu do pliku.

Ustawiamy tożmasość dla puli aplikacji:
	- wchodzimy w IIS menager
	- wchodzimy w pule aplikacji
	- szukamy takiej przypisanej do naszej nowej witryny
	- plikamy ustawienia zaawansowane
	- szukamy opcji tożsamość (trzeba zjechać scrollem, jest w sekcji modele procesów)
	- ustawiamy na naszego pierwszego nowoutworzonego użytkownika 

Teraz po uruchomieniu strony, część backendowa aplikacji uruchamia się
z uprawnieniami pierwszego użytkownika, więc możemy otworzyć plik bo tak ustawiliśmy jego zabepieczenia.

Identycznie jak wcześniej zmieniamy tożsamość strony na drugiego utworzonego przez nas użytkownika
i pokazujemy, że mamy znowu odmowę dostępu do pliku.










