# Notatka z wykładu: Kodowanie i szyfrowanie

## Typy kodów detekcyjnych

- **Bit parzystości** – wykrywa błędy z nieparzystą liczbą przekłamań.
- **Prosta suma kontrolna** – sumowanie słów, wykrywa niektóre błędy; nie wykrywa zamiany słów.
- **CRC (Cyclic Redundancy Check)** – oparty na wielomianach, skuteczny i powszechnie stosowany (np. w Ethernecie).

## Rodzaje błędów transmisji

- Przekłamania bitów (pojedynczych lub ciągów),
- Zgubione lub wstawione bity,
- Błędy sprzętowe (RAM, oprogramowanie).

## Algorytm CRC – jak działa

1. Zamieniamy wiadomość m na wielomian M(x),
2. Obliczamy xr · M(x) i dzielimy przez G(x),
3. Reszta z dzielenia to suma kontrolna S(x),
4. Wysyłamy B(x) = xr · M(x) + S(x),
5. Odbiorca sprawdza, czy G(x) dzieli B'(x).

## Wykrywanie błędów CRC

- G(x) ∤ B’(x) ⇒ błąd transmisji,
- Wiele typów błędów jest wykrywanych, np. pięć kolejnych przekłamań.

## Metody korekcji błędów

- **Kody korekcyjne** – pozwalają również na poprawę błędów,
- **Kod Hamminga (np. (7,4))** – wykrywa 2 błędy, koryguje 1,
- **(3,1)-kod** – powtarzanie każdego bitu 3 razy (mało efektywne).

## (a,b)-kod – definicja i przykład

- Kodowanie wiadomości długości b na długość a ≥ b,
- Przykład: bit parzystości dla 7 bitów to (8,7)-kod,
- Narzut = a/b.

## Odległość Hamminga

- Minimalna liczba bitów, jakie trzeba zmienić między dwoma kodami,
- Kod o odległości ≥ k:
  - wykrywa do k-1 błędów,
  - koryguje do (k-1)/2 błędów.

## Kody MAC i HMAC

- **MAC** – wykrywa celowe modyfikacje wiadomości,
- **HMAC** – bezpieczna wersja MAC: h(s#h(s#m)),
- Wykorzystywany w TLS, OpenVPN itp.

## Cechy funkcji skrótu

- Jednokierunkowość,
- Trudność znalezienia kolizji,
- Szybkość działania,
- Deterministyczność.

## Poufność vs integralność

- **Poufność** – ochrona treści (szyfrowanie),
- **Integralność** – wykrywanie modyfikacji (np. CRC, MAC).

## Szyfry monoalfabetyczne

- Proste podstawienie liter (np. Cezara, ROT13),
- Łatwe do złamania analizą częstotliwości.

## Typy ataków kryptograficznych

- **Wybrany tekst jawny** – atakujący wybiera tekst,
- **Znany tekst jawny** – zna pary (tekst, szyfrogram),
- **Znany szyfrogram** – zna tylko szyfrogram.

## Szyfrowanie one-time pad

- m XOR K, klucz tak długi jak wiadomość,
- Teoretycznie idealne, praktycznie trudne (zarządzanie kluczem).

## Szyfrowanie blokowe – ECB vs CBC

- **ECB** – każdy blok szyfrowany niezależnie, identyczne bloki = identyczny szyfrogram,
- **CBC** – każdy blok zależy od poprzedniego, używa IV, bezpieczniejsze.
