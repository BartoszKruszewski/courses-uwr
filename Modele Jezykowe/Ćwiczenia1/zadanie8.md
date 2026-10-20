# Zadanie 8

1. **Mieszanie rozkładów (ta sama tokenizacja):** w każdym kroku p = λ·p₁ + (1−λ)·p₂ (albo iloczyn/średnia logitów). Wariant *contrastive decoding*: log p_duży − α·log p_mały.
2. **Generuj i rerankuj (dowolna tokenizacja):** model A generuje N kandydatów (zdań lub fragmentów), a model B ocenia je swoim log P po **tekście**. Wybieramy najlepszy wg sumy ocen obu modeli. Działa na poziomie stringów, więc tokenizacja jest bez znaczenia.
3. **Mieszanie na poziomie słów (różne tokenizacje):** każdy model proponuje kilka następnych **całych wyrazów** (zad. 5), oba liczą P(wyraz | prefiks) jako iloczyn swoich tokenów, wyniki łączymy i wybieramy wyraz.
