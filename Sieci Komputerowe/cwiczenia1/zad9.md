Załóżmy, że mamy sieć:

```
       C
      / \
     A---B
      \ /
       D
```

---

Załóżmy, że **łącze między A i B ulega awarii**.

1. **A i B natychmiast się o tym dowiadują** i **rozgłaszają aktualizację**.
2. **Informacja o awarii propaguje się stopniowo** do pozostałych routerów C i D.

Załóżmy, że **router C już dostał informację o awarii**, ale router D jeszcze nie.

3. **C widzi, że łącze A-B jest zerwane**, więc jeśli ma przesłać pakiet do D, wybierze ścieżkę **C → A → D**.

4. **D jeszcze nie dostał informacji o awarii**, więc wciąż widzi starą topologię, gdzie łącze A-B istnieje. Jeśli dostanie pakiet przeznaczony dla A, może go wysłać **do B, ponieważ myśli, że łącze A-B działa**. Następnie **B, który już wie o awarii, przekieruje pakiet z powrotem do D przez inne dostępne ścieżki**.

W ten sposób **pakiet może krążyć w nieskończonej pętli**, zanim wszystkie routery zsynchronizują swoją wiedzę o sieci.
