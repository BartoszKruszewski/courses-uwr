# Textbooks Are All You Need: ściąga do prezentacji

Ta ściąga tłumaczy prostymi słowami, co trzeba wiedzieć do każdego slajdu z `slides.md`. Numery odpowiadają kolejności slajdów.

- **[PAPER]** oznacza, że informacja pochodzi z pracy (Gunasekar i in., Microsoft Research, czerwiec 2023).
- **🟠 [WEB]** oznacza wiedzę spoza pracy, zebraną z internetu (stan na październik 2026).
- **[TŁO]** to ogólna wiedza o LLM-ach. Nie ma jej w pracy wprost, ale przydaje się, żeby zrozumieć temat.

---

## 1. Tytuł: *Textbooks Are All You Need*

**[PAPER]**
- Praca z Microsoft Research, opublikowana w czerwcu 2023 (arXiv 2306.11644). Wśród autorów są m.in. Sébastien Bubeck, Ronen Eldan i Yuanzhi Li.
- Przedstawia model **phi-1**, od którego zaczęła się cała rodzina modeli **Phi**.
- Tytuł nawiązuje do słynnej pracy *Attention Is All You Need* (2017), w której zaproponowano Transformera. Tutaj „wszystkim, czego potrzebujesz” nie jest nowa architektura, tylko **dobre dane, napisane jak podręcznik**.

**Plan wystąpienia:** najpierw praca (ok. 33 minut), potem to, co stało się później (ok. 10 minut, slajdy z pomarańczowym znaczkiem).

---

## 2. „What if better data beats bigger models?”

**[PAPER]**
- Główna teza: zamiast powiększać model albo trenować go dłużej, można **poprawić jakość danych** i dostać podobny lub lepszy efekt dużo mniejszym kosztem.
- Autorzy zwracają też uwagę na ekologię: mniejszy model i krótszy trening to mniej prądu i mniejszy ślad węglowy.

**Pomysł na otwarcie:** zapytaj salę, czy jakość modelu zależy bardziej od jego rozmiaru, czy od danych.

---

## 3. Scaling laws

**[TŁO]**
- **Prawa skalowania** (Kaplan i in., 2020): błąd (*loss*) modelu językowego spada przewidywalnie, zgodnie z prawem potęgowym, gdy zwiększamy liczbę parametrów, ilość danych albo moc obliczeniową. Na wykresie w skali logarytmicznej wygląda to jak prosta linia w dół.
- **Chinchilla** (Hoffmann i in., 2022) pokazała, że wcześniejsze modele były „niedotrenowane”. Dla danej mocy obliczeniowej trzeba proporcjonalnie zwiększać i model, i liczbę tokenów.
- Przez te prawa branża przez lata skupiała się na hasłach „więcej parametrów” i „więcej danych”.

**[PAPER]**
- Autorzy pytają, co się stanie, jeśli zmienimy trzecią rzecz, czyli **jakość danych**.
- Inspiracją była praca **TinyStories** (Eldan i Li, 2023, ci sami autorzy). Wygenerowali tam syntetyczne, proste opowiadania dla dzieci i pokazali, że **bardzo małe modele** (kilka–kilkadziesiąt milionów parametrów) potrafią pisać płynnym angielskim. Wniosek: dobre dane mogą zmienić **kształt** krzywej skalowania, a nie tylko przesunąć punkt na niej.
- phi-1 sprawdza, czy ten pomysł działa w prawdziwym zadaniu, czyli w programowaniu, i na poziomie najlepszych modeli.

---

## 4. The domain: code

**[PAPER] + [TŁO]**
- Zadanie: model dostaje nagłówek funkcji w Pythonie i **docstring** (opis słowami, co funkcja ma robić), a musi napisać jej ciało.
- **HumanEval** (OpenAI, praca o Codexie, 2021): 164 ręcznie napisane zadania. Każde ma testy jednostkowe i rozwiązanie jest poprawne tylko wtedy, gdy przechodzi wszystkie testy.
- **MBPP** (*Mostly Basic Python Problems*, Google, 2021): ok. 1000 prostych zadań programistycznych, też sprawdzanych testami.
- **pass@1**: model ma jedną próbę i liczy się procent zadań rozwiązanych za pierwszym razem. To surowa miara: prawie dobry kod to dalej zero punktów.
- Kod jest wygodną dziedziną do takich badań, bo poprawność da się sprawdzić automatycznie.

---

## 5. phi-1 at a glance

**[PAPER]**
- **1,3 mld parametrów**, co jak na rok 2023 jest małym modelem. Konkurencja miała od 15 do 540 mld.
- **Mniej niż 7 mld tokenów** unikalnych danych. Model przeszedł po nich ok. 8 razy (8 epok), więc łącznie „zobaczył” ok. 50 mld tokenów.
- **Mniej niż 4 dni** treningu na 8 kartach NVIDIA A100 plus 7 godzin dotrenowania (*finetuningu*). Taki budżet ma uczelniane laboratorium, nie wielka firma.
- Wynik: **50,6% na HumanEval** i **55,5% na MBPP**, czyli jeden z najlepszych wyników przy jednej próbie w połowie 2023.
- Mniejsza wersja, **phi-1-small** (350 mln parametrów), też osiągnęła 45% na HumanEval.

**[TŁO]** *Token* to kawałek tekstu, mniej więcej część słowa. W kodzie tokenem bywa nazwa zmiennej, nawias, wcięcie itd.

---

## 6. HumanEval vs open & closed models

**[PAPER] (Tabela 1)**
- Wyraźnie lepszy od phi-1 jest tylko **GPT-4** (67%).
- **WizardCoder** (16 mld) ma lepszy HumanEval (57,3%), ale gorsze MBPP (51,8% wobec 55,5%).
- phi-1 wyprzedza **GPT-3.5** (175 mld, 47%), **PaLM-Coder** (540 mld, 35,9%), **StarCodera** (15,5 mld, 33,6–40,8%) i **Codex-12B** (28,8%).
- Konkurenci trenowali na **100 mld – 1 bln tokenów**, a phi-1 na 7 mld, czyli ok. 100 razy mniej.
- Zastrzeżenie: w tabeli są wyniki **deklarowane przez autorów** poszczególnych modeli, nie mierzone niezależnie.

---

## 7. Size vs score

**[PAPER] (dane z Tabeli 1)**
- Każda kropka to jeden model. Oś X to liczba parametrów w skali logarytmicznej, oś Y to wynik na HumanEval.
- Szare kropki układają się w trend: większy model, lepszy wynik.
- phi-1 (niebieska kropka) leży **daleko nad trendem** jak na swój rozmiar. To obrazowa wersja hasła „łamiemy prawa skalowania”.
- Podsumowanie autorów: **10× mniejszy model, 100× mniej danych**, a wynik porównywalny lub lepszy.

---

## 8. What's wrong with web code?

**[PAPER]**
- Standardowe zbiory danych z kodem:
  - **The Stack**: ok. 3 TB kodu z GitHuba na otwartych licencjach,
  - **StackOverflow**: pytania i odpowiedzi programistów,
  - **CodeContests**: zadania konkursowe.
- Są ogromne i różnorodne, ale autorzy przejrzeli losowe próbki i znaleźli 4 problemy:
  1. **Kod nie jest samowystarczalny**: zależy od innych plików i modułów, więc bez kontekstu nic nie wiadomo.
  2. **Dużo kodu „pustego”**: definicje stałych, konfiguracja, ustawianie GUI, bez żadnej logiki.
  3. **Logika jest zakopana** w długich, nieudokumentowanych funkcjach.
  4. **Tematy są nierówno rozłożone**: niektórych umiejętności jest masa, innych prawie wcale.
- Analogia autorów: człowiek uczący się programowania z takich danych byłby sfrustrowany, bo dostaje szum zamiast nauki. Autorzy zakładają, że model ma ten sam problem.

---

## 9. High vs low educational value

**[PAPER]**
- Oba przykłady pochodzą z pracy.
- **Wysoka wartość edukacyjna** (po lewej): funkcja z docstringiem, która coś naprawdę liczy (odległość kosinusową), jest krótka i samowystarczalna.
- **Niska wartość** (po prawej): klasa, która tylko ustawia kilkanaście pól (`self._winid = -1` itd.). Nie ma tu żadnego algorytmu ani nic, czego dałoby się nauczyć.
- Pytanie do sali: z którego przykładu nauczylibyście się programować?

---

## 10. A good textbook is clear, self-contained, instructive, balanced

**[PAPER]**
- Cztery cechy dobrych danych, będące odwrotnością 4 problemów z poprzedniego slajdu:
  - **clear**: jasne,
  - **self-contained**: zrozumiałe bez dodatkowego kontekstu,
  - **instructive**: uczą czegoś konkretnego,
  - **balanced**: obejmują wszystkie tematy w rozsądnych proporcjach.
- Od tego pomysłu pochodzi tytuł: dane mają przypominać **dobry podręcznik**.

---

## 11. The data recipe

**[PAPER]**
Model trenowano na trzech zbiorach danych, łącznie mniej niż 7 mld tokenów:
1. **Przefiltrowany kod z internetu**: ok. 6 mld tokenów (fragment The Stack i StackOverflow).
2. **Syntetyczne podręczniki**: mniej niż 1 mld tokenów, wygenerowane przez GPT-3.5.
3. **CodeExercises**: ok. 180 mln tokenów ćwiczeń z rozwiązaniami, też z GPT-3.5.

- Zbiory 1+2 razem to **CodeTextbook**. Na nich robi się *pretraining* (trening od zera) i powstaje **phi-1-base**, który ma już 29% na HumanEval.
- Zbiór 3 służy do *finetuningu* (krótkiego dotrenowania), po którym powstaje **phi-1**.
- Architektura jest celowo zwyczajna. Cały wkład pracy dotyczy **danych**.

**[TŁO]** *Pretraining* to długi trening na dużym zbiorze, w którym model uczy się przewidywać kolejny token. *Finetuning* to krótkie dotrenowanie gotowego modelu na mniejszym, wyspecjalizowanym zbiorze.

---

## 12. Step 1: Filter the web

**[PAPER]**
- Na start: pythonowa część The Stack (po deduplikacji, czyli usunięciu powtórzonych plików) plus StackOverflow, łącznie **35 mln plików i 35 mld tokenów**.
- **GPT-4** dostał ok. **100 tys. próbek** i miał ocenić ich „wartość edukacyjną dla ucznia, który chce nauczyć się podstaw programowania”.
- Na tych ocenach wytrenowano prosty klasyfikator, **las losowy** (*random forest*), który przewiduje jakość pliku.
- Klasyfikator nie czyta tekstu bezpośrednio. Dostaje **embedding** pliku, czyli wektor liczb opisujący treść kodu, policzony przez wstępnie wytrenowany model CodeGen.
- Taki klasyfikator jest bardzo tani, więc można nim ocenić wszystkie 35 mln plików. Zostaje ok. **6 mld tokenów**.
- Dlaczego tak? GPT-4 jest drogi, więc używa się go tylko do etykietowania małej próbki, zamiast zatrudniać ludzi. Resztę robi tani model.

**Ważne na później:** ten pomysł został potem powszechnie skopiowany (FineWeb-Edu, slajd 34).

**[TŁO]** *Las losowy* to klasyczny algorytm uczenia maszynowego: wiele drzew decyzyjnych głosuje nad odpowiedzią.

---

## 13. Filtering alone helps

**[PAPER]**
Eksperyment na małym modelu (350 mln parametrów), wyniki na HumanEval:
- **Bez filtrowania**: wynik zatrzymuje się na **12,19%**, nawet po 96 tys. kroków treningu (ok. 200 mld tokenów).
- **Z filtrowaniem**: **17,68%** już po 36 tys. kroków.
- **Filtrowanie i syntetyczne podręczniki**: **20,12%**.

Wniosek: **mniej, ale lepszych danych daje lepszy model.**

---

## 14. Step 2: Synthetic textbooks, diversity

**[PAPER]**
- GPT-3.5 napisał mniej niż 1 mld tokenów „podręczników do Pythona”: tekst wyjaśniający przeplatany fragmentami kodu, nastawiony na **rozumowanie i podstawowe algorytmy**.
- **Główny problem to różnorodność.** Jeśli 1000 razy poprosisz model o „napisz podręcznik programowania”, dostaniesz prawie to samo, bo modele wybierają najbardziej prawdopodobną ścieżkę. Taki zbiór sprzyja zapamiętywaniu zamiast uogólniania.
- **Sposób autorów:** do każdego zapytania (*promptu*) dodają losowość, czyli **losowy temat i losowego odbiorcę** (np. „dla początkującego”, „dla studenta matematyki”).
- W TinyStories robiono podobnie: model dostawał losowe słowa, które musiał wpleść w opowiadanie.
- **Słaby punkt pracy:** dokładnych promptów **nie opublikowano** („z powodów własnościowych”), więc trudno odtworzyć wyniki.

---

## 15. A synthetic textbook page

**[PAPER]**
- Prawdziwy, skrócony fragment syntetycznego podręcznika: definicja macierzy osobliwej (wyznacznik równy zero), wyjaśnienie i przykład w kodzie.
- Ciekawostka do omówienia: `det == 0` dla liczb zmiennoprzecinkowych jest ryzykowne, bo wyznacznik może wyjść np. 1e-17 zamiast 0. **Dane z GPT-3.5 mają sporo błędów**, co autorzy sami przyznają.
- Mimo to model uczy się dobrze. Autorzy przewidują, że dane z GPT-4 byłyby jeszcze lepsze, i to się później sprawdziło (Phi-4, slajd 32).

---

## 16. Step 3: CodeExercises

**[PAPER]**
- Ok. **180 mln tokenów**, ok. **880 tys. ćwiczeń**: każde ma docstring, a model ma dopisać ciało funkcji.
- Format jest **taki sam jak w HumanEval**. Celem jest nauczyć model pisania funkcji na podstawie opisu słownego.
- Różnorodność uzyskano przez **narzucanie różnych nazw funkcji** w promptach.
- Ćwiczenia korzystają tylko z **podstawowych bibliotek** (math, random, typing, collections…).
- Skoro format przypomina HumanEval, pojawia się podejrzenie, że model po prostu „widział testy”. Autorzy sprawdzają to dokładnie na slajdach 22–26.

---

## 17. Model & training

**[PAPER] + [TŁO]**
- **Decoder-only Transformer**, czyli taki sam typ jak GPT: model czyta tekst od lewej do prawej i przewiduje kolejny token.
- phi-1: 24 warstwy, wymiar ukryty 2048, 32 głowice uwagi. phi-1-small: 20 warstw, wymiar 1024, 16 głowic.
- Zastosowane techniki:
  - **FlashAttention**: szybsza i oszczędniejsza pamięciowo implementacja mechanizmu uwagi; wynik jest ten sam, liczy się szybciej,
  - **równoległe MHA + MLP**: warstwa uwagi i warstwa MLP liczą się równolegle, a nie jedna po drugiej, jak w PaLM czy CodeGen,
  - **RoPE** (*rotary position embeddings*): sposób kodowania pozycji tokenu w zdaniu przez „obracanie” wektorów.
- Świadomie **pominięte** sztuczki, które mogłyby jeszcze poprawić wynik:
  - **FIM** (*Fill-In-the-Middle*): trening uzupełniania kodu w środku pliku,
  - **MQA** (*Multi-Query Attention*): wspólne klucze i wartości dla wszystkich głowic, co przyspiesza generowanie.
- Chodziło o to, żeby było jasne, że wynik daje **dane, a nie sztuczki**.
- Trening: kontekst 2048 tokenów, AdamW, fp16, DeepSpeed, 8× A100.
  - Pretraining: punkt kontrolny po 24 tys. krokach, czyli ok. 8 epok i ok. 50 mld tokenów, mniej niż 4 dni.
  - Finetuning: 6 tys. kroków, 7 godzin.

---

## 18. The key experiment (Figure 2.1)

**[PAPER]**
Trzy grupy słupków odpowiadają klasycznym sposobom skalowania:
- **350M, 26 mld tokenów** → **350M, 76 mld tokenów**: więcej obliczeń, ten sam model,
- → **1,3B**: większy model.

W każdej grupie są trzy kolory danych:
- **szary**: standardowe dane (The Stack+), które prawie nie poprawiają się wraz ze skalą (11 → 12 → 17),
- **fioletowy**: CodeTextbook, wyraźnie lepsze (16 → 20 → 29),
- **czarny lub zielony**: CodeTextbook i dotrenowanie na CodeExercises, ogromny skok (41 → 45 → **51**).

Najważniejsze liczby dla modelu 1,3B: **17 → 29 → 51**. Model trenowany na zwykłych danych dostał nawet **więcej** obliczeń (1090 wobec 770 godzin GPU), a i tak był dużo słabszy.

---

## 19. 180M tokens of exercises: 29% → 51%

**[PAPER]**
- **Najmniejszy zbiór daje największy skok:** mniej niż 200 mln tokenów i 7 godzin treningu.
- Dla porównania: poprzednio najmniejszy model z wynikiem ok. 30% to Replit-Finetuned. Ma 2,7 mld parametrów i trenował na ok. 100 razy większej liczbie tokenów.
- Ten slajd prowadzi do dwóch pytań:
  1. Czy dotrenowanie daje **nowe umiejętności**? (slajdy 20–21)
  2. Czy to nie jest po prostu **zapamiętanie testu**? (slajdy 22–26)

---

## 20. Emergent skills: understanding

**[PAPER] (sekcja 3)**
- Ta część jest **jakościowa**: autorzy rozmawiają z modelem i porównują jego odpowiedzi, podobnie jak w pracy „Sparks of AGI” o GPT-4.
- **Emergentna umiejętność** to taka, której model nie uczył się wprost, a mimo to ją ma.
- **Hipoteza autorów:** dotrenowanie na prostych ćwiczeniach „porządkuje” wiedzę zdobytą w pretrainingu i pozwala jej użyć.
- Przykład: Alicja, Bob i Karol losują liczby z różnych zakresów, a punkty zależą od podzielności przez pierwiastek. Model ma zasymulować 30 rund.
  - **phi-1**: poprawna pętla i warunek.
  - **phi-1-base**: wypisuje w kółko `self.alice = …`, `self.bob_points = …` i nigdy nie rozwiązuje zadania.
  - **phi-1-small**: rozumie ogólną ideę, ale myli zakresy, więc logika jest błędna.

---

## 21. Emergent skills: libraries

**[PAPER]**
- W ćwiczeniach **nie było** bibliotek PyGame (gry) ani Tkinter (okienka GUI), a mimo to phi-1 radzi sobie z nimi dużo lepiej niż phi-1-base.
- **PyGame** (piłka poruszająca się losowo w ramce):
  - phi-1-base zna funkcje PyGame, ale **nie realizuje zadania**,
  - phi-1-small **rozumie logikę**, ale nie zna API,
  - phi-1 umie jedno i drugie.
- **Tkinter** (aplikacja z polem tekstowym i przyciskami): phi-1 robi wszystko dobrze, poza jedną literówką („pewpewpew…” zamiast „pewpewpew?”). Pozostałe modele wymyślają nieistniejące funkcje, np. `tk.popup()`.
- W dodatku A są też przykłady z PyTorchem (aktualizacja wag przez SVD) i animacją w pyplot.
- **Chat** (pytanie studenta do asystenta): phi-1 odpowiada jak asystent na ćwiczeniach, krokami i z przykładem. Uwaga krytyczna: używa `ax.rotate(90)`, a **taka funkcja w matplotlib nie istnieje**. Lepsza odpowiedź nie znaczy poprawna.
- **Wniosek o rozmiarze:** phi-1-small przeszedł identyczny trening, ale tych umiejętności nie ma. **Emergencja wymaga odpowiedniej liczby parametrów**, więc lepsze dane nie znoszą znaczenia rozmiaru modelu.

---

## 22. Memorization? 50 new problems

**[PAPER] (sekcja 4)**
- **Obawa:** CodeExercises mają ten sam format co HumanEval. Może GPT-3.5, który znał HumanEval, wygenerował bardzo podobne zadania? Wtedy wynik oznaczałby zapamiętanie, a nie umiejętność. Nazywa się to **kontaminacją danych** (*contamination*): dane testowe przeciekają do treningowych.
- **Odpowiedź 1:** osobny zespół, który **nie miał dostępu** ani do danych, ani do modelu, napisał **50 nowych zadań**, specjalnie dziwnych i nietypowych. Przykład ze slajdu: posortuj dwie listy, połącz je, podnieś do kwadratu elementy na parzystych indeksach, odfiltruj małe i usuń duplikaty. Takiej kombinacji nie da się zapamiętać.
- **Ocena przez GPT-4:** zamiast testów zaliczone/niezaliczone GPT-4 porównuje kod z poprawnym rozwiązaniem, pisze krótką ocenę słowną i wystawia **0–10 punktów**. To trochę jak rozmowa rekrutacyjna, na której ocenia się też tok rozumowania.
  - Zalety: dokładniejsza ocena (prawie dobry kod dostaje część punktów) i nie trzeba pisać testów.
  - Wada **[TŁO]**: LLM jako sędzia ma własne skrzywienia. Może np. faworyzować pewien styl kodu.

---

## 23. Same ranking on new problems

**[PAPER] (Tabela 2)**
- Na nowych zadaniach **kolejność modeli jest taka sama** jak na HumanEval.
- phi-1: **52%**, StarCoder (15,5B): 51%. Tutaj różnica jest mała, a na HumanEval była duża (51 wobec 34).
- phi-1-small (350M): 45%, czyli lepiej niż CodeGen 16B (38%).
- Zadania celowo wykraczały poza to, co model mógł widzieć, więc wynik **zwiększa zaufanie**, że phi-1 naprawdę umie programować.

---

## 24. n-gram overlap

**[PAPER] (sekcja 5.1)**
- **N-gram** to ciąg n kolejnych słów. Standardowy test kontaminacji sprawdza, czy jakieś 13 kolejnych słów z HumanEval występuje w danych treningowych.
- Wynik: tylko **4 trafienia** i wszystkie fałszywe. Na przykład oba teksty zawierały to samo ogólne zdanie „the frequency of an integer is the number of times it appears in the list”, ale zadania były zupełnie inne.
- **Problem:** n-gramy wyłapują tylko kopiowanie słowo w słowo. Zadanie przepisane innymi słowami przejdzie niezauważone. Dlatego autorzy idą dalej.

---

## 25. Prune anything similar

**[PAPER] (sekcja 5.2)**
Ten slajd i wykres na slajdzie 26 to jedno badanie. Autorzy szukają w CodeExercises zadań **podobnych** do HumanEval na dwa sposoby:
- **Odległość embeddingów**: oba kawałki kodu zamienia się na wektory (model CodeGen) i sprawdza, czy leżą blisko. Wyłapuje to podobieństwo **znaczenia**.
- **Odległość AST**: AST (*abstract syntax tree*) to drzewo składni programu. Porównanie drzew wyłapuje **taką samą strukturę kodu**, nawet przy innych nazwach zmiennych i komentarzach. Parametr **τ** (tau) to próg podobieństwa: im niższy, tym luźniej rozumiane „podobne” i tym więcej zadań się usuwa.

Potem **usuwają podobne zadania i trenują model od nowa** na tym, co zostało. Przy τ = 0,8 usunięto **354 tys. z 879,5 tys. ćwiczeń (ok. 40%)**, w tym zadania tylko luźno podobne. To bardzo agresywna wersja usuwania kontaminacji (*decontamination*).

---

## 26. Still beats StarCoder

**[PAPER] (Tabela 3)**
- Nawet po usunięciu 40% danych phi-1 ma **45,1%**, a StarCoder **41,5%**.
- Wynik spadł z 50,6% do ok. 45%, więc podobne zadania **trochę pomagały**. Autorzy uczciwie to pokazują.
- Ciekawostka z tabeli: **wszystkie** modele, także StarCoder, który nie widział tych danych, lepiej radzą sobie z zadaniami „podobnymi”. Możliwe, że te zadania są po prostu łatwiejsze i bardziej typowe.
- Wniosek: przewaga phi-1 **nie wynika z kontaminacji**, nawet w luźnym sensie tego słowa.

---

## 27. Limitations

**[PAPER] (dodatek B)**
- **Zakres:** tylko Python. Model zna mniej rzadkich bibliotek niż duże modele i nie napisze np. złożonej aplikacji we Flasku.
- **Długie prompty:** sieć z 3 warstwami napisze dobrze, z 4 już się wyłoży, a po dopisaniu na początku `import torch` znowu działa. Ćwiczenia były krótkie, więc model gubi się przy długich poleceniach, a drobna zmiana potrafi odwrócić wynik.
- **Język:** literówki i błędy gramatyczne mocno obniżają skuteczność. Słowo „unchanged” („x stays unchanged”) model zrozumiał jako `x = 0`. Numerowane listy w poleceniu też go mylą.
- **Liczenie i układ przestrzenny:** poproszony o 2 pola tekstowe i 3 przyciski w określonym układzie, robi 3 pola i źle ustawia przyciski.
- **Ogólny kompromis:** dane czyste jak w podręczniku dają model słabiej odporny na „brudne” polecenia prawdziwych ludzi.

---

## 28. Open problems they name

**[PAPER] (wnioski)**
- **Pokrycie (coverage):** jak zapewnić, że dane obejmują wszystkie potrzebne pojęcia w dobrych proporcjach?
- **Różnorodność (diversity):** jak uniknąć powtórzeń?
- **Pomiar (measurement):** nie umiemy dobrze **zmierzyć** różnorodności i redundancji zbioru danych.
- **Etyka:** jeśli LLM-y będą tworzyć dane dla kolejnych LLM-ów, pojawiają się pytania o przejrzystość, odpowiedzialność i powielanie uprzedzeń (*bias*).
- Autorzy wspominają debatę o „rekurencyjnym treningu” (modele uczone na danych z modeli mogą się zawężać) i zaznaczają, że przy wąskim zadaniu uczeń może przegonić nauczyciela.
- **Praca w jednym zdaniu:** model 10× mniejszy, 100× mniej danych, wynik bliski najlepszym w kodzie.

**Przejście:** „To był czerwiec 2023. Zobaczmy, co było dalej.”

---

## 29. 🟠 What happened next (slajd działowy)

**[WEB]** Od tego miejsca wszystko pochodzi spoza pracy: z raportów technicznych Microsoftu, blogów i artykułów. Na każdym takim slajdzie jest pomarańczowy znaczek. Warto to powiedzieć na głos.

---

## 30. 🟠 The Phi family

**[WEB]**
- **phi-1** (czerwiec 2023): 1,3B, kod, ta praca.
- **phi-1.5** (wrzesień 2023, raport „Textbooks Are All You Need II”): też 1,3B, ale ten sam przepis zastosowano do **zdroworozsądkowego rozumowania i języka naturalnego**, nie tylko do kodu.
- **phi-2** (grudzień 2023): 2,7B, 1,4 bln tokenów. Microsoft twierdził, że dorównuje modelom do 25× większym.
- **Phi-3** (kwiecień 2024): wersje mini (3,8B), small (7B) i medium (14B). **Phi-3-mini** miał **69% na MMLU**, mniej więcej poziom GPT-3.5, i działał **na telefonie**.
- **Phi-3.5** (sierpień 2024): doszła wersja **MoE** i wersja z obrazami.
- **Phi-4** (grudzień 2024): 14B, dane w większości syntetyczne (szczegóły na slajdzie 32).
- **Phi-4-mini** i **Phi-4-multimodal** (luty 2025): 3,8B oraz 5,6B, ta druga obsługuje tekst, obraz i mowę.
- **Phi-4-reasoning** (kwiecień 2025): 14B, model „myślący”, który pisze tok rozumowania przed odpowiedzią.
  - Powstał przez dotrenowanie na zapisach rozumowań modelu **o3-mini** od OpenAI.
  - Wersja „plus” przeszła dodatkowo krótkie uczenie ze wzmocnieniem (RL).
  - Według autorów jest lepszy od 5× większego DeepSeek-R1-Distill-Llama-70B w większości testów.
- **Phi-4-mini-flash-reasoning** (lipiec 2025): 3,8B z architekturą hybrydową, według Microsoftu do 10× większa przepustowość.
- **Phi-4-reasoning-vision** (marzec 2026): 15B, tekst i obraz, **sam decyduje, czy myśleć**.
  - Ok. 20% danych treningowych miało znacznik `<think>` (z rozumowaniem), a 80% znacznik `<nothink>` (odpowiedź od razu).
  - Rozumuje przy matematyce, a od razu odpowiada np. przy czytaniu tekstu z obrazka.
  - Trenowany na ok. 200 mld tokenów multimodalnych, podczas gdy konkurenci zużyli ponad 1 bln.

**[TŁO]**
- **MMLU**: test wiedzy z 57 dziedzin (pytania wielokrotnego wyboru).
- **MoE** (*Mixture of Experts*): model ma wiele podsieci, tzw. ekspertów, ale dla każdego tokenu uruchamia tylko kilka z nich. Ma więc dużo parametrów, a liczy się tanio.

---

## 31. 🟠 Small model ≠ small data anymore

**[WEB]**
- phi-1 słynął z **bardzo małej ilości danych** (7 mld tokenów).
- Kolejne modele Phi trenowano już na **bilionach** tokenów: phi-2 na 1,4 bln, Phi-3-mini na 3,3 bln, Phi-4 na ok. 10 bln.
- **Wniosek:** z tezy pracy przetrwała część „**lepsze** dane”, a nie przetrwała część „**mało** danych”. Dziś wygrywa jakość i ilość jednocześnie.
- Wykres ma skalę logarytmiczną, więc słupek o tej samej wysokości oznacza 10× więcej.

---

## 32. 🟠 Phi-4: student beats teacher

**[WEB] (Phi-4 Technical Report, grudzień 2024)**
- 14B parametrów. **Większość danych do pretrainingu to dane syntetyczne**, ok. 400 mld tokenów w ok. 50 rodzajach zbiorów.
- Techniki generowania są dużo bogatsze niż „losowy temat” z phi-1:
  - **multi-agent prompting**: kilka instancji modelu współpracuje lub dyskutuje,
  - **self-revision**: model poprawia własne odpowiedzi,
  - **instruction reversal**: z gotowej odpowiedzi odtwarza się pasujące polecenie.
- Dane w dużej mierze generował **GPT-4o**, a Phi-4 pokonał swojego „nauczyciela” w dwóch testach:
  - **GPQA** (trudne pytania z nauk ścisłych na poziomie doktoratu): 56,1 wobec 50,6,
  - **MATH** (zadania z konkursów matematycznych): 80,4 wobec 74,6.
- Praca o phi-1 sugerowała, że w wąskim zadaniu uczeń może przegonić nauczyciela, i tu to się stało.
- Autorzy wyciągnęli też wniosek z problemu kontaminacji: testowali na konkursach **AMC-10/12 z listopada 2024**, które odbyły się już po zebraniu danych, więc model na pewno ich nie widział.
- Zastrzeżenie: liczby GPQA i MATH sprawdziłem w źródle wtórnym. Warto je potwierdzić w Tabeli 1 raportu.

---

## 33. 🟠 Phi today: October 2026

**[WEB]**
- **Phi-5 nie ma.** Microsoft go nie ogłosił, a „poradniki o Phi-5” w internecie to spekulacje. Linia Phi-4 jest rozwijana w wyspecjalizowanych wersjach: rozumowanie, obraz, szybkie modele na urządzenia.
- **Gdzie działa Phi:**
  - **Phi Silica** jest wbudowany w Windows na komputerach Copilot+ PC i działa lokalnie na NPU (specjalnym chipie do AI),
  - Azure AI Foundry (chmura),
  - Hugging Face i Ollama: otwarte wagi na licencji **MIT**, można je pobrać i uruchomić u siebie.
- **Ludzie:** Sébastien Bubeck, współautor pracy i lider Phi, przeszedł do **OpenAI w październiku 2024**. Według doniesień większość współautorów została w Microsofcie.
- Microsoft rozwija też własne duże modele **MAI**. Phi to dział „małych modeli”.

---

## 34. 🟠 Impact: “educational value” filters

**[WEB] (FineWeb, Penedo i in., 2024)**
- Hugging Face powtórzył pomysł filtra z phi-1 na **danych z całego internetu**, nie tylko na kodzie:
  1. **Llama-3-70B** oceniła ok. 450 tys. stron w skali 0–5 pod względem wartości edukacyjnej.
  2. Na tych ocenach wytrenowano mały klasyfikator.
  3. Klasyfikator przefiltrował cały zbiór FineWeb i zostawił strony z oceną ≥ 3, czyli ok. **1,3 bln tokenów** (zbiór **FineWeb-Edu**).
- Wyniki: **MMLU wzrosło z 33% do 37%**, a **ARC** (pytania naukowe na poziomie szkolnym) z **46% do 57%**.
- W odróżnieniu od Microsoftu Hugging Face **opublikował** dane i klasyfikator.
- Według pracy FineWeb tej samej techniki użyto przy trenowaniu Llamy 3 i Phi-3.

---

## 35. 🟠 Impact: synthetic data goes mainstream

**[WEB]**
- **Otwarte podręczniki, Cosmopedia → SmolLM:** Hugging Face próbował odtworzyć dane phi-1.5. Model Mixtral wygenerował ok. 25 mld tokenów podręczników, wpisów blogowych, opowiadań i poradników. Dane i kod są publiczne. Kolejna wersja (Cosmopedia v2) stała się główną częścią danych dla małych modeli **SmolLM**.
- **Przepisywanie internetu (rephrasing):** zamiast generować wszystko od zera, model językowy **przepisuje istniejące strony** na lepszą formę: pytania i odpowiedzi, tutoriale, listy. To pośrednia droga między filtrowaniem a generowaniem.
  - Przykłady: **WRAP**, **Nemotron-CC** (NVIDIA), **BeyondWeb** (DatologyAI). Dziś to standardowa praktyka.
  - Badania z 2026 pokazują, że **ustrukturyzowane formaty** (tabele, FAQ, tutoriale) wypadają lepiej niż starannie dobrane strony internetowe. Styl podręcznika znowu wygrywa.
- **Destylacja, czyli „nauczyciel pisze podręcznik”:** duży model generuje dane treningowe dla małego.
  - GPT-4o → Phi-4,
  - o3-mini → Phi-4-reasoning,
  - **DeepSeek-R1** (styczeń 2025) → małe modele R1-Distill (oparte na Qwen i Llamie).
- **Małe modele są dziś wszędzie:** Phi-4, Gemma 3 (Google), Qwen3 (Alibaba), Llama 3.2 1B/3B (Meta), SmolLM3 (Hugging Face). Wszystkie mocno opierają się na selekcji i syntetycznych danych, a **przepis na dane** to dziś główna przewaga konkurencyjna, często trzymana w tajemnicy.

**[TŁO]** *Destylacja wiedzy* to uczenie małego modelu („ucznia”) na odpowiedziach dużego („nauczyciela”).

---

## 36. 🟠 Critiques

**[WEB]**
- **Parodia „Pretraining on the Test Set Is All You Need”** (Rylan Schaeffer, wrzesień 2023): żartobliwa praca o modelu „phi-CTNL” z 1 mln parametrów, który „bije wszystko”, bo trenowano go na danych testowych. Wprost nawiązuje do phi-1.5. Kpi z podejrzeń, że syntetyczne dane za bardzo przypominają testy.
- **Benchmarki a wrażenia z użycia:** użytkownicy często zgłaszali, że modele Phi świetnie wypadają w testach, a gorzej w swobodnej rozmowie i nietypowych zadaniach. Pasuje to do ograniczeń z samej pracy, czyli słabej odporności na „brudne” polecenia. Microsoft z czasem zaczął np. testować na świeżych konkursach (Phi-4) i publikować logi ewaluacji (2026).
- **Model collapse** (Shumailov i in., *Nature* 2024): jeśli model trenuje się na **własnych** wynikach przez wiele pokoleń, jego jakość spada, a rzadkie przypadki znikają z rozkładu.
- **Kontrargument:** w praktyce dane syntetyczne, które są **różnorodne**, filtrowane, weryfikowane i **mieszane z prawdziwymi**, działają dobrze. Kluczem jest różnorodność, czyli dokładnie to, czym martwili się autorzy phi-1.

---

## 37. 🟠 Did the paper's claims hold up?

**[WEB], podsumowanie oceny**

| Teza pracy | Dziś |
|---|---|
| jakość danych zmienia prawa skalowania | ✓ powszechnie przyjęte |
| dane generowane przez LLM działają | ✓ standardowa praktyka |
| filtry jakości z etykietami od LLM | ✓ FineWeb-Edu, Llama 3 |
| wystarczy mało danych | ✗ Phi trenuje dziś na bilionach tokenów |
| benchmarki oddają prawdziwe umiejętności | ~ wciąż sporne |

- Rozmiar modelu nadal ma znaczenie, co pokazała już sama praca: phi-1-small nie miał emergentnych umiejętności.

---

## 38. Takeaways

1. **Jakość danych to osobna oś skalowania**, obok rozmiaru modelu i mocy obliczeniowej: 10× mniejszy model i 100× mniej danych.
2. **Małe, dobrze dobrane dotrenowanie może dać nowe umiejętności**: 180 mln tokenów podniosło wynik z 29% do 51% i dało emergentne użycie bibliotek.
3. **Kontaminację trzeba sprawdzać poważnie**: nowe zadania, n-gramy, agresywne usuwanie podobnych przykładów. To dobry wzór dla innych prac.
- Bonus: pomysł z tej pracy jest dziś wszędzie (FineWeb-Edu, Phi-4, destylacja).

---

## 39. Thank you / Questions?

Możliwe pytania i krótkie odpowiedzi:
- **Czy ocena przez GPT-4 jest uczciwa?** Daje dokładniejszy sygnał niż zaliczone/niezaliczone i ranking zgadza się z HumanEval. LLM jako sędzia ma jednak własne skrzywienia, a GPT-4 może faworyzować pewien styl kodu.
- **Dlaczego nie opublikowano danych?** Autorzy powołują się na „powody własnościowe”. Otwartą alternatywą jest Cosmopedia od Hugging Face.
- **Czy to działa dla innych języków programowania lub zadań?** phi-1.5 i kolejne modele pokazały, że przepis działa też dla języka naturalnego i rozumowania. Sam phi-1 był jednak tylko pythonowy.
- **Czy GPT-3.5 nie znał HumanEval?** Mógł znać, dlatego autorzy zrobili test na 50 nowych zadaniach i agresywnie usuwali podobne przykłady. Po usunięciu 40% danych model i tak był lepszy od StarCodera.
- **Dlaczego dotrenowanie daje tak duży skok?** To hipoteza, nie dowód: ćwiczenia „porządkują” wiedzę z pretrainingu i uczą wykonywać polecenia. Model miał wiedzę, ale nie umiał jej użyć.
- **Czy to nie zwykła destylacja z GPT-3.5?** Częściowo tak, bo dane pisał GPT-3.5. Nowością było to, **jakie** dane generować (styl podręcznika, różnorodność) i połączenie tego z filtrowaniem prawdziwych danych.

---

## 40. Sources

Pokaż ten slajd tylko wtedy, gdy ktoś zapyta. Pomarańczowy znaczek „web” przy pozycji oznacza źródło spoza pracy.
