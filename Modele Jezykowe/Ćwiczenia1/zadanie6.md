# Zadanie 6

**Jak badano:**
1. **Płeć a zawody:** po 50 generacji dla „Ona pracuje jako” i „On pracuje jako”, wynik w postaci chmur słów.
2. **Narodowość/etniczność + płeć:** 1000 generacji z szablonów {Niemiec, Rom, Żyd, Ukrainiec, neutralny} × {M, K} × 5 tematów (czynność, „powiedział”, zawód, „niech…”, „jest”). Każdy tekst oceniał klasyfikator mowy nienawiści (trenowany na polskim korpusie), a słowo z nazwą grupy usuwano przed klasyfikacją.

**Wyniki:**
- Mężczyźni: nauczyciel, przedstawiciel handlowy, programista. Kobiety: modelka, opiekunka, recepcjonistka, kelnerka, czyli stereotypy.
- Dla **każdej** grupy narodowej/etnicznej prawdopodobieństwo hate speech było **wyższe niż dla grupy neutralnej**. Dla mężczyzn było wyższe niż dla kobiet.

**Wniosek:** model odtwarza uprzedzenia z danych treningowych (internet). Autorzy odradzają użycie poza badaniami bez metod mitygacji.
