# Przypadek użycia: **Złożenie zamówienia w sklepie internetowym**

## 1. Nazwa przypadku użycia:  
**Złożenie zamówienia**

## 2. Aktorzy:  
- **Klient** – osoba przeglądająca produkty i składająca zamówienie.  
- **System sklepu internetowego** – obsługuje proces przeglądania produktów, dodawania do koszyka, finalizacji zamówienia oraz przetwarzania płatności.  
- **System płatności** – zewnętrzny system obsługujący płatności online.  
- **Magazyn** – system odpowiedzialny za aktualizację stanów magazynowych oraz wysyłkę produktów.  

## 3. Opis:  
Przypadek użycia opisuje proces składania zamówienia w sklepie internetowym. Klient przegląda produkty, dodaje je do koszyka, wprowadza dane do wysyłki, wybiera metodę płatności oraz finalizuje zamówienie. Po dokonaniu płatności, system sklepu internetowego przekazuje zamówienie do magazynu.

## 4. Warunki początkowe:  
- Klient jest zalogowany w sklepie internetowym (lub jako gość).  
- Produkty dostępne w sklepie mają wystarczający stan magazynowy.  

## 5. Warunki końcowe:  
- **Sukces:** Zamówienie zostaje złożone, a klient otrzymuje potwierdzenie. Stan magazynowy produktów zostaje zaktualizowany.  
- **Niepowodzenie:** Klient zostaje poinformowany o problemie (np. brak towaru, nieudana płatność), zamówienie nie jest finalizowane.  

## 6. Przepływ podstawowy (scenariusz główny):  
1. Klient przegląda produkty w sklepie internetowym.  
2. Klient dodaje wybrane produkty do koszyka.  
3. Klient przechodzi do koszyka i sprawdza zawartość.  
4. Klient klika **"Przejdź do kasy"**.
5. System prosi o podanie danych wysyłkowych i wyboru metody płatności.  
6. Klient wprowadza dane wysyłkowe i wybiera metodę płatności.  
7. Klient klika **"Złóż zamówienie"**.  
8. System sklepu internetowego przekazuje dane do systemu płatności.  
9. System płatności przetwarza płatność i zwraca wynik do systemu sklepu.  
10. Jeśli płatność przebiegła pomyślnie, system sklepu:  
    - Potwierdza złożenie zamówienia klientowi.  
    - Aktualizuje stan magazynowy produktów.  
    - Przekazuje zamówienie do systemu magazynowego.  
11. Klient otrzymuje potwierdzenie złożenia zamówienia drogą mailową.  

## 7. Przepływy alternatywne:  
- **7a.** Klient nie uzupełnił wszystkich danych wysyłkowych:  
   - System wyświetla komunikat o brakujących danych.  
   - Klient uzupełnia dane i ponownie klika **"Złóż zamówienie"**.  

- **9a.** Płatność nie powiodła się:  
   - System informuje klienta o nieudanej płatności.  
   - Klient może wybrać inną metodę płatności lub anulować zamówienie.  

- **10a.** Brak produktów na stanie magazynowym:  
   - System informuje klienta o braku produktów.  
   - Klient może usunąć brakujący produkt z koszyka lub anulować zamówienie.  

## 8. Wymagania specjalne:  
- Dane klienta muszą być przetwarzane zgodnie z RODO.  
- System musi być odporny na ataki typu **"man-in-the-middle"** podczas przetwarzania płatności.  
- Potwierdzenie zamówienia powinno być wysyłane w ciągu 5 minut od jego złożenia.  

## 9. Częstotliwość użycia:  
Kilka razy dziennie w zależności od popularności sklepu.

## 10. Uwagi i założenia:  
- Klient ma możliwość dokonania zakupu bez rejestracji (jako gość).  
- System płatności jest niezależny od systemu sklepu internetowego (zewnętrzna integracja).  
