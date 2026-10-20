# Zadanie 2

## a

Najlepszy w ogóle: **Gemini-4-Argon – 97.33**.

Najlepszy z otwartymi wagami: **Muse-Spark-Open – 91.67**.

## b

Bielik-4.5B-v3.0-Instruct: ~42.3%

następny to Qwen3.5-4B, ~29.7%

## c

**Art & entertainment**

Pytania dotyczą polskich filmów, literatury, sportu, mediów i sztuki, czyli szczegółów polskiej popkultury. Są trudne, bo to rzadka wiedza z „długiego ogona”, słabo reprezentowana w danych treningowych, które są głównie angielskie.

## d

- Sortowanie alfabetyczne
- Ortografia

## e

Ortografia lub poprawianie błędów: generujemy wszystkie warianty (o_ydny → ohydny/ochydny), a mały LM liczy **log P zdania lub słowa** dla każdego z nich. Wybieramy wariant o najwyższym prawdopodobieństwie, normalizując po liczbie tokenów.
