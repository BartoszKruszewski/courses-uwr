import os
import re
import warnings

# mute warnings
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
warnings.filterwarnings("ignore")

from transformers import pipeline  # noqa: E402

MODEL_NAME = "sdadas/polish-gpt2-medium"

print(f"Loading model {MODEL_NAME} ...")
generator = pipeline(
    "text-generation",
    model=MODEL_NAME,
    device=-1,  # CPU
)
print("Model ready!\n")

preamble = (
    "Oto zapis rozmowy między Użytkownikiem a Asystentem.\n"
    "Użytkownik zadaje pytania na dowolny temat,"
    "a Asystent odpowiada w sposób zwięzły, "
    "konkretny i rzeczowy, używając języka polskiego.\n\n"
)

history = []
MAX_TURNS = 6

FORBIDDEN_ENDINGS = {
    "które", "który", "która", "oraz", "i", "a", "ale", "że", "ponieważ",
    "bo", "jak", "więc", "dla", "do", "w", "z", "o", "na", "po", "lub", "to", "czy"
}


def clean_first_sentence(raw_text: str) -> str:
    text = raw_text.strip()
    text = re.sub(r"^[\.\s,\-—:]+", "", text)

    # Cut off if the model attempts to generate conversational turns or newlines
    for delim in ["\n", "Użytkownik:", "Asystent:"]:
        if delim in text:
            text = text.split(delim)[0].strip()

    # Extract the first sentence terminating with . ! ?
    match = re.search(r"^(.*?[.!?])", text)
    if match:
        candidate = match.group(1).strip(' "—\t')
        words = candidate.rstrip(".!?").split()
        if words and words[-1].lower() in FORBIDDEN_ENDINGS:
            return ""
        return candidate

    return ""


def score_candidate(cand: str, user_msg: str) -> float:
    if not cand:
        return -100.0

    words = re.findall(r"\w+", cand.lower())
    if len(words) < 2:
        return -100.0

    score = 0.0

    # Target length for an informative single-sentence reply
    word_count = len(words)
    if 4 <= word_count <= 16:
        score += 20.0
    elif 17 <= word_count <= 22:
        score += 6.0
    else:
        score -= 10.0

    # Complete terminal punctuation
    if cand.endswith((".", "!", "?")):
        score += 15.0

    # Topical keyword overlap (words with 3+ characters)
    q_words = set(re.findall(r"\w{3,}", user_msg.lower()))
    cand_words = set(re.findall(r"\w{3,}", cand.lower()))
    score += len(cand_words.intersection(q_words)) * 6.0

    # Lexical diversity
    score += (len(set(words)) / word_count) * 10.0

    return score


def ask_assistant(user_msg: str) -> str:
    # Build prompt using bounded rolling history
    prompt = preamble
    for speaker, text in history[-MAX_TURNS:]:
        prompt += f"{speaker}: {text}\n"
    prompt += "Asystent:"

    # Generate multiple sampled sequences for scoring
    outputs = generator(
        prompt,
        max_new_tokens=32,
        do_sample=True,
        temperature=0.4,
        top_p=0.85,
        repetition_penalty=1.35,
        no_repeat_ngram_size=2,
        num_return_sequences=4,
        pad_token_id=generator.tokenizer.eos_token_id,  # type: ignore
        clean_up_tokenization_spaces=False,
    )

    # Rank and pick the candidate with the highest score
    candidates = []
    for out in outputs:
        tail = out["generated_text"][len(prompt):]
        clean_ans = clean_first_sentence(tail)
        val = score_candidate(clean_ans, user_msg)
        candidates.append((clean_ans, val))

    candidates.sort(key=lambda x: x[1], reverse=True)
    best_answer = candidates[0][0]

    # Fallback in case all outputs were pruned or empty
    if not best_answer:
        best_answer = "Trudno mi jednoznacznie odpowiedzieć na to pytanie."

    return best_answer


while True:
    try:
        user_input = input("Użytkownik: ").strip()
    except (KeyboardInterrupt, EOFError):
        break

    if not user_input:
        continue

    history.append(("Użytkownik", user_input))
    answer = ask_assistant(user_input)
    history.append(("Asystent", answer))
    print(f"Asystent: {answer}\n")
