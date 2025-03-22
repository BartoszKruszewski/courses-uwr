# Zadanie: Stylizacja Strony (10p)

Twoim zadaniem będzie ostylowanie strony zgodnie z poniższymi wytycznymi. Stylizacja powinna zostać zaimplementowana **wyłącznie przy użyciu CSS**. Możesz edytować kod HTML tylko w wyznaczonych miejscach opisanych przez komentarz. Ostateczny wygląd strony powinien zgadzać się z [obrazkiem](./sol.png) ([pełna rozdzielczość](./blog_fullres.png)).

## Materiały

Oprócz materiałów które można znaleźć na [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS) warto przećwiczyć selektory i specyficzność z użyciem [CSS dinner](https://flukeout.github.io/) oraz [CSS speedrun](https://css-speedrun.netlify.app/).

W szczególności, własności użyte w rozwiązaniu wzorcowym to: `background-color`, `border`, `border-color`, `border-radius`, `border-top`, `border-top-color`, `box-sizing`, `color`, `content`, `display`, `font-family`, `font-size`, `font-weight`, `list-style`, `margin`, `max-width`, `min-width`, `text-align`, `text-decoration`, `width`

---

## **Styl ogólny**: Aplikowane do całej strony

- Ustaw kolor tła strony na `lightblue`, a kolor tekstu na `darkblue`.
- Wybierz dowolną czcionkę z [Google Fonts](https://fonts.google.com/) i ustaw ją dla całej strony. W tym celu dodaj odpowiedni link do sekcji `<head>` w pliku HTML.
- Wszystkie nagłówki `h1` powinny mieć grubość czcionki `800`.
- Paragrafy (`<p>`) powinny mieć marginesy z każdej strony – wartości marginesów z prawej i lewej strony powinny być równe i większe od zera. Marginesy powinny rosnąć wraz z wielkością czcionki elementu `html`.
- Ustaw domyślną wielkość czcionki na `1rem`.
- Nagłówek (`h1`) powinien być wyśrodkowany w poziomie.

## **Pudełka**: Sekcja "Boxes" (id="challenge2")

- W sekcji `"boxes"` znajdują się trzy pudełka:

  - **Pierwsze pudełko** powinno mieć kolor `lightgreen` i być okręgiem.
  - **Drugie pudełko** powinno mieć kolor `lightslategray` oraz czarne obramowanie o grubości `10px`. Razem z obramowaniem powinno mieć rozmiar `100px x 100px`.
  - **Trzecie pudełko** powinno być do połowy białe, a od połowy czerwone.

- Interakcje najechania myszką ([gif](./hover.gif)):

  - **Pierwsze pudełko** po najechaniu zmienia kolor na `lightpink`.
  - **Drugie pudełko** po najechaniu powinno mieć czarny środek i `lightslategray` obramowanie.
  - **Trzecie pudełko** po najechaniu powinno zmieniać kolory na odwrotne (góra czerwona, dół biały).

- **By uzyskać pełną liczbę punktów nie należy bezpośrednio modyfikować wysokości czy szerokości pudełek**.

## **Stylizacja linków**: Sekcja "Links" (id="challenge3")

- Linki powinny mieć ten sam kolor co tekst (`darkblue`).
- Odwiedzone linki powinny mieć kolor `lightslategray`.
- Po najechaniu myszką, linki powinny być czerwone, pogrubione i zawsze podkreślone.
- Zamiast kropek, elementy listy powinny używać ikony "🍔".

## **Ukrywanie elementów**: Sekcja "Too much" (id="challenge4")

Ukryj następujące elementy:

- Puste paragrafy (`<p></p>`).
- Wyłączone (`disabled`) pola `<input>`.
- Linki zawierające w adresie fragment `"recipe"`.

Ukrywanie powinno działać także dla nowo dodanych elementów i nie powinno zależeć od ich kolejności w kodzie.

## **Responsywny obrazek**: Sekcja "Images" (id="challenge5")

- Szerokość obrazka powinna wynosić **70% dostępnej przestrzeni**.
- Minimalna szerokość: `100px`.
- Maksymalna szerokość: `500px`.
- Podpis pod obrazkiem (`<figcaption>`) powinien mieć rozmiar **`0.7`** wartości czcionki elementu `html`.