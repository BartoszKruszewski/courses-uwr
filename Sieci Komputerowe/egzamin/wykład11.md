# Notatka z wykładu: Podstawy kryptografii – Szyfrowanie i Uwierzytelnianie

## 1. Różnica między szyfrowaniem symetrycznym a asymetrycznym
- **Symetryczne**: ten sam klucz do szyfrowania i deszyfrowania, efektywne obliczeniowo, ale trudne w dystrybucji klucza.
- **Asymetryczne**: dwa różne klucze – publiczny do szyfrowania, prywatny do deszyfrowania; łatwiejsza dystrybucja kluczy.

## 2. Bezpieczeństwo szyfrowania asymetrycznego
- Opiera się na problemach trudnych obliczeniowo (np. rozkład liczby na czynniki).
- Znajomość klucza publicznego nie umożliwia odczytania wiadomości.

## 3. Algorytm RSA
1. Wybór dwóch dużych liczb pierwszych `p` i `q`.
2. Obliczenie `n = p * q` i `φ(n) = (p - 1) * (q - 1)`.
3. Wybór `e` względnie pierwszego z `φ(n)`.
4. Obliczenie `d` takiego, że `d * e ≡ 1 (mod φ(n))`.
5. Klucz publiczny: `(e, n)`, prywatny: `(d, p, q)`.
6. Szyfrowanie: `c = m^e mod n`, deszyfrowanie: `m = c^d mod n`.

## 4. Różnica: szyfrowanie vs uwierzytelnianie
- **Szyfrowanie** zapewnia poufność.
- **Uwierzytelnianie** zapewnia, że wiadomość pochodzi od deklarowanego nadawcy.

## 5. Atak powtórzeniowy
- Adwersarz przechwytuje podpisaną wiadomość i odtwarza ją później.
- Obroną jest użycie losowego wyzwania (nonce).

## 6. Klucze w szyfrowaniu asymetrycznym
- **Szyfrowanie**: klucz publiczny odbiorcy.
- **Deszyfrowanie**: klucz prywatny odbiorcy.

## 7. Podpisywanie wiadomości
- Tworzy się podpis: `Ea(h(m))`, czyli szyfrowana funkcja skrótu.
- Podpis wykonuje się kluczem **prywatnym**, a weryfikuje kluczem **publicznym**.

## 8. Podpisy cyfrowe a uwierzytelnianie
- Podpis potwierdza tożsamość nadawcy (tylko on zna klucz prywatny).
- Weryfikacja podpisu potwierdza autentyczność.

## 9. HMAC a podpisy cyfrowe
- HMAC = `h(s # h(s # m))`, używa sekretu znanego obu stronom.
- HMAC nie jest podpisem cyfrowym – nie zapewnia niezaprzeczalności.

## 10. Podpisywanie funkcji skrótu vs całej wiadomości
- Lepsze: podpisywać `h(m)` – krótsze, szybsze.
- Ryzyko: kolizje funkcji skrótu → możliwość ataków (np. atak urodzinowy).

## 11. Certyfikaty i ścieżka certyfikacji
- **Certyfikat** = powiązanie klucza publicznego z tożsamością, podpisane przez zaufany podmiot.
- **Ścieżka certyfikacji** = ciąg zaufanych podpisów prowadzących do danego certyfikatu.

## 12. Urząd certyfikacji (CA)
- Wydaje certyfikaty, jego klucze publiczne są znane i zaufane (wbudowane w przeglądarki).

## 13. Bezpieczeństwo TLS
- TLS szyfruje dane i uwierzytelnia strony.
- Używa asymetrycznego szyfrowania do ustanowienia sesji, potem symetrycznego.

## 14. Uwierzytelnienie serwera w TLS
- Sprawdzenie certyfikatu podpisanego przez CA.
- Przeglądarka ufa CA, weryfikuje klucz serwera.

## 15. Klucze sesji
- Symetryczne klucze generowane przez klienta.
- Wysyłane zaszyfrowane kluczem publicznym serwera.

## 16. Kolizje funkcji skrótu
- Dwie różne wiadomości mają ten sam hash.
- Prowadzi do potencjalnych ataków (np. podmiana treści).

## 17. Atak urodzinowy
- Łatwiej znaleźć dwie różne wiadomości o tym samym skrócie niż jedną konkretną.
- Wymaga około `2^(n/2)` prób dla n-bitowego skrótu.
