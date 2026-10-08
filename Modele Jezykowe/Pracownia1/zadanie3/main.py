import os
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


def construct_prompt_recommendation(text):
    pos = f"{text} Polecam to miejsce."
    neg = f"{text} Odradzam to miejsce."
    return pos, neg


def construct_prompt_evaluation(text):
    pos = f"Opinia: {text}\nOcena: pozytywna."
    neg = f"Opinia: {text}\nOcena: negatywna."
    return pos, neg


def construct_prompt_sentiment_word(text):
    pos = f"{text} Wrażenia były bardzo dobre."
    neg = f"{text} Wrażenia były bardzo złe."
    return pos, neg


def classify_opinion(text, template_fn):
    pos_str, neg_str = template_fn(text)

    score_pos = sentence_prob(pos_str)
    score_neg = sentence_prob(neg_str)

    # Usuwamy bias samego sufiksu
    dummy_pos, dummy_neg = template_fn("")
    bias_pos = sentence_prob(dummy_pos)
    bias_neg = sentence_prob(dummy_neg)

    calibrated_pos = score_pos - bias_pos
    calibrated_neg = score_neg - bias_neg

    return "positive" if calibrated_pos > calibrated_neg else "negative"


def evaluate_method(dataset, template_fn):
    correct = 0
    for text, label in dataset:
        predicted_label = classify_opinion(text, template_fn)
        if predicted_label == label:
            correct += 1
    return correct / len(dataset)


opinions_positive = [
    "Parking monitorowany w cenie.",
    "Hotel czysty, pokoje były sprzątane bardzo dokładnie.",
    "Generalnie mogę go polecić, kierował mnie na potrzebne badania, analizował ich wyniki.",
    "Fajny klimat pofabrykanckich kamienic.",
    "Sala zabaw dla dzieci, plac zabaw na zewnątrz, kominek, tenis stołowy.",
    "Świetna lokalizacja w samym centrum miasta, wszędzie blisko na piechotę.",
    "Obsługa niezwykle pomocna i uprzejma na każdym kroku.",
    "Pyszne, urozmaicone śniadania podawane w formie bufetu.",
    "Widok z okna zapierał dech w piersiach, na pewno wrócimy.",
    "Bardzo cicha i spokojna okolica, idealna na odpoczynek.",
]

opinions_negative = [
    "W wielu pokojach niedziałająca klimatyzacja.",
    "Jedzenie mimo rzekomych dni europejskich monotonne.",
    "Drożej niż u konkurencji w podobnym standardzie.",
    "Może za szybko zrezygnowałam, ale szkoda mi było wydawać pieniędzy na spotkania, które nie przynosiły efektu.",
    "Omijaj to miejsce!",
    "Łazienka była brudna, a pościel sprawiała wrażenie nieświeżej.",
    "Hałas z ulicy uniemożliwiał spokojny sen przez całą noc.",
    "Personel na recepcji bardzo opryskliwy i niezainteresowany gośćmi.",
    "Ceny w restauracji kosmiczne w stosunku do miniaturowych porcji.",
    "Zimna woda pod prysznicem rano, usterka nie została naprawiona.",
]

dataset = [(text, "positive") for text in opinions_positive] + [
    (text, "negative") for text in opinions_negative
]

for template_fn in [
    construct_prompt_recommendation,
    construct_prompt_evaluation,
    construct_prompt_sentiment_word,
]:
    print(
        f"Accuracy '{template_fn.__name__}': {evaluate_method(dataset, template_fn):.2%}"
    )
