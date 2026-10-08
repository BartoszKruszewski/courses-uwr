import os
import warnings
from itertools import permutations

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

sentence = "Babuleńka miała dwa rogate koziołki."
words = sentence.lower()[:-1].split(" ")
sentence_permutations = [
    " ".join(permutation).capitalize() + "." for permutation in permutations(words)
]
permutation_probs = {perm: sentence_prob(perm) for perm in sentence_permutations}
for perm in sorted(
    sentence_permutations, key=lambda x: permutation_probs[x], reverse=True
):
    print(f"{perm} -> {permutation_probs[perm]}")
