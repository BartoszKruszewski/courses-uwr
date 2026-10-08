import os
import random
import re
import warnings

import torch
from torch.nn import functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer

# mute warnings
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
warnings.filterwarnings("ignore")

model_name = "flax-community/papuGaPT2"
device = "cuda"
device = "cpu"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)  # type: ignore


def log_probs_from_logits(logits, labels):
    logp = F.log_softmax(logits, dim=-1)
    logp_label = torch.gather(logp, 2, labels.unsqueeze(2)).squeeze(-1)
    return logp_label


def sentence_prob(sentence_txt):
    input_ids = tokenizer(sentence_txt, return_tensors="pt")["input_ids"].to(device)
    with torch.no_grad():
        output = model(input_ids=input_ids)
        log_probs = log_probs_from_logits(output.logits[:, :-1, :], input_ids[:, 1:])
        seq_log_probs = torch.sum(log_probs)
    return seq_log_probs.cpu().numpy()


# To co powyzej jest z wykladu


def heuristic_answer(q):
    m = re.search(
        r"([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ0-9\s\-]+?)\s+czy\s+([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ0-9\s\-]+)\??$",
        q.strip(),
    )
    if m:
        return m.group(1).strip()
    if q.lower().startswith("czy ") and " czy " not in q.lower()[4:]:
        return "tak"
    return None


CENTURIES = [
    "I",
    "II",
    "III",
    "IV",
    "V",
    "VI",
    "VII",
    "VIII",
    "IX",
    "X",
    "XI",
    "XII",
    "XIII",
    "XIV",
    "XV",
    "XVI",
    "XVII",
    "XVIII",
    "XIX",
    "XX",
    "XXI",
]


def prob_based_answer(q):
    if "którym wieku" in q.lower():
        scores = {
            c: sentence_prob(f"Pytanie: {q} Odpowiedź: w {c} wieku.")
            for c in CENTURIES
        }
        return f"w {max(scores, key=scores.get)}"  # type: ignore
    return None


FEW_SHOT = """
Pytanie: Kto napisał "Pana Tadeusza"?\n
Odpowiedź: Adam Mickiewicz\n
Pytanie: Ile nóg ma pies?\n
Odpowiedź: 4\n
Pytanie: {q}\n
Odpowiedź:
"""


def few_shot_answer(q):
    inp = tokenizer(FEW_SHOT.format(q=q), return_tensors="pt")["input_ids"].to(device)
    with torch.no_grad():
        gen = model.generate(  # type: ignore
            input_ids=inp, max_new_tokens=6, pad_token_id=tokenizer.eos_token_id
        )
    return (
        tokenizer.decode(gen[0][inp.shape[1]:], skip_special_tokens=True)
        .split("\n")[0]
        .strip()
    )


def solve(q):
    return heuristic_answer(q) or prob_based_answer(q) or few_shot_answer(q)


with (
    open("questions.txt", encoding="utf-8") as fq,
    open("answers.txt", encoding="utf-8") as fa,
):
    data = list(
        zip(
            [line.strip() for line in fq if line.strip()],
            [line.strip().split("\t") for line in fa if line.strip()],
        )
    )

sample = random.sample(data, 50)
correct = sum(
    any(solve(q).lower() in a.lower() or a.lower() in solve(q).lower() for a in ans)
    for q, ans in sample
)
print(f"Accuracy: {correct / len(sample):.1%}")
