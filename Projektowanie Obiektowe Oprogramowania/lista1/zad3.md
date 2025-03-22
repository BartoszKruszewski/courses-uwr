# Model pojęciowy: System Rezerwacji Stanowisk w Pokoju Wspólnym w Akademiku

## 1. **Użytkownik**
- **Opis**: Osoba korzystająca z systemu rezerwacji. Może to być student zamieszkujący akademik.
- **Atrybuty**:
  - Imię
  - Nazwisko
  - Email
  - Numer pokoju
- **Powiązania**:
  - Może dokonywać wielu **Rezerwacji**
  - Może posiadać jedno **Konto**

## 2. **Konto**
- **Opis**: Konto użytkownika w systemie, umożliwia logowanie i zarządzanie rezerwacjami.
- **Atrybuty**:
  - Login
  - Hasło (zaszyfrowane)
  - Status aktywności
- **Powiązania**:
  - Należy do jednego **Użytkownika**

## 3. **Rezerwacja**
- **Opis**: Proces zajmowania stanowiska przez użytkownika na określony czas.
- **Atrybuty**:
  - Data rozpoczęcia
  - Data zakończenia
  - Status (np. aktywna, anulowana, zakończona)
- **Powiązania**:
  - Jest powiązana z jednym **Użytkownikiem**
  - Dotyczy jednego **Stanowiska**

## 4. **Stanowisko**
- **Opis**: Miejsce pracy w pokoju wspólnym, które można zarezerwować.
- **Atrybuty**:
  - Numer stanowiska
  - Rodzaj (np. biurko, miejsce do pracy w grupie)
  - Dostępność (np. dostępne, zajęte)
- **Powiązania**:
  - Może być zarezerwowane przez wiele **Rezerwacji**
  - Znajduje się w jednym **Pokoju**

## 5. **Pokój**
- **Opis**: Przestrzeń wspólna w akademiku zawierająca stanowiska do pracy.
- **Atrybuty**:
  - Numer pokoju
  - Opis (np. pokój cichy, pokój do pracy w grupie)
- **Powiązania**:
  - Zawiera wiele **Stanowisk**

## 6. **Powiadomienie**
- **Opis**: Wiadomość wysyłana do użytkownika w związku ze statusem rezerwacji.
- **Atrybuty**:
  - Typ (np. potwierdzenie rezerwacji, przypomnienie, anulowanie)
  - Treść wiadomości
  - Data wysłania
- **Powiązania**:
  - Jest powiązane z jedną **Rezerwacją**
  - Jest wysyłane do jednego **Użytkownika**

## 7. **Administrator**
- **Opis**: Osoba zarządzająca systemem rezerwacji, mająca uprawnienia do moderacji użytkowników i stanowisk.
- **Atrybuty**:
  - Imię
  - Nazwisko
  - Email
  - Poziom uprawnień
- **Powiązania**:
  - Może zarządzać wieloma **Rezerwacjami**
  - Może zarządzać wieloma **Stanowiskami**

## Powiązania między pojęciami:
- **Użytkownik** → dokonuje → **Rezerwacja**
- **Użytkownik** → posiada → **Konto**
- **Rezerwacja** → dotyczy → **Stanowisko**
- **Stanowisko** → znajduje się w → **Pokój**
- **Rezerwacja** → generuje → **Powiadomienie**
- **Administrator** → zarządza → **Rezerwacja**
- **Administrator** → zarządza → **Stanowisko**

## Opis modelu:
Model pojęciowy opisuje system rezerwacji stanowisk w pokoju wspólnym akademika. W systemie istnieje sześć głównych pojęć: **Użytkownik**, **Konto**, **Rezerwacja**, **Stanowisko**, **Pokój**, **Powiadomienie** oraz **Administrator**. Każde z pojęć posiada swoje atrybuty oraz powiązania z innymi pojęciami. Model ten uwzględnia zależności oraz relacje, które występują w rzeczywistym systemie rezerwacji, zapewniając spójność oraz możliwość dalszej rozbudowy.