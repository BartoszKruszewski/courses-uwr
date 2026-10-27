import random
from math import comb

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "flax-community/papuGaPT2"
tok = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).eval()
N = 200  # liczba zadań w każdym eksperymencie

# Swobodna generacja (model.generate) dawała wyniki na poziomie losowym, bo model
# "uciekał" w inny tekst (np. "3 + 4 = 8ROZDZIAŁ I..."). Dlatego model wybiera
# odpowiedź spośród liczb 0..max - każda liczba " k" (k < 1000) to jeden token,
# więc wystarczy jeden forward pass i argmax po tych tokenach.


def answer(prompt, max_ans):
    ids = tok(prompt, return_tensors="pt").input_ids
    with torch.no_grad():
        logits = model(ids).logits[0, -1]
    cands = [tok(f" {k}").input_ids[0] for k in range(max_ans + 1)]
    return logits[cands].argmax().item()


def p_value(hits, p):  # P(X >= hits), X ~ Bin(N, p) - szansa, że losowe zgadywanie da taki wynik
    return sum(comb(N, k) * p**k * (1 - p) ** (N - k) for k in range(hits, N + 1))


def experiment(name, make_task, max_ans, shots=5, intro=""):
    random.seed(0)  # ten sam seed => te same liczby w każdym wariancie (porównanie parami)
    hits = 0
    for _ in range(N):
        examples = [make_task() for _ in range(shots + 1)]
        prompt = intro + "".join(f"{q} {a}, " for q, a in examples[:-1]) + examples[-1][0]
        hits += answer(prompt, max_ans) == examples[-1][1]
    base = 1 / (max_ans + 1)
    print(f"{name:25} acc={hits / N:4.0%}  losowo={base:5.1%}  p={p_value(hits, base):.0e}")


def arith(op, hi):
    def task():
        a, b = sorted([random.randint(0, hi), random.randint(0, hi)], reverse=True)  # a >= b, by a - b >= 0
        return f"{a} {op} {b} =", eval(f"{a} {op} {b}")
    return task


print("=== Eksperyment 1: rodzaj działania i wielkość liczb (5-shot) ===")
experiment("a + b, a,b < 10", arith("+", 9), 18)
experiment("a - b, a,b < 10", arith("-", 9), 9)
experiment("a * b, a,b < 10", arith("*", 9), 81)
experiment("a + b, a,b < 100", arith("+", 99), 198)
experiment("a - b, a,b < 100", arith("-", 99), 99)

print("\n=== Eksperyment 2: liczba przykładów w prompcie (a + b, a,b < 10) ===")
for shots in [0, 1, 3, 5, 10]:
    experiment(f"{shots}-shot", arith("+", 9), 18, shots)

print("\n=== Eksperyment 3: bias - imię w prompcie (a * b, a,b < 10) ===")
for who in ["Jan", "Piotr", "Anna", "Maria", "Mohammed", "Aisha", "John", "Mary"]:
    experiment(who, arith("*", 9), 81, intro=f"{who} liczy: ")

# Wyniki (papuGaPT2, N=200, seed 0):
#   Eksp. 1: +  <10: 12% (losowo 5.3%), -  <10: 14% (10%), *  <10: 15% (1.2%),
#            + <100: 1% (0.5%),         - <100: 2% (1%)
#   Eksp. 2: 0/1/3/5/10-shot: 0% / 8% / 8% / 12% / 12%
#   Eksp. 3: wszystkie imiona 14-16%
#
# Wnioski:
# 1. Model jest istotnie lepszy od losowego zgadywania dla działań na cyfrach,
#    najwyraźniej dla mnożenia (15% vs 1.2%, p ~ 1e-23). Nawet uczciwszy baseline -
#    losowanie spośród 37 możliwych iloczynów cyfr (2.7%) - jest daleko poniżej 15%.
#    Tabliczka mnożenia często występuje w tekstach, więc model ją częściowo "pamięta".
# 2. Dla liczb dwucyfrowych model praktycznie nie umie liczyć (wynik ~ losowy).
# 3. Przykłady w prompcie pomagają: 0-shot = 0% (model nie wie, że ma podać wynik),
#    od ~5 przykładów wynik się stabilizuje na ~12%.
# 4. Swobodna generacja nie działała (model dopisywał inny tekst) - ograniczenie
#    odpowiedzi do liczb było kluczowe. Format też ma znaczenie: separator ", "
#    działał lepiej niż "\n", a mniejszy papuGaPT2 lepiej niż polish-gpt2-medium.
# 5. Bias: różnice między imionami (męskie/żeńskie, polskie/obce) to 14-16%, czyli
#    max 4 zadania na 200 - mieści się w szumie (odch. std. ~2.5 p.p.). Przy tych
#    samych zadaniach dla każdego imienia nie zaobserwowano obciążenia modelu.
