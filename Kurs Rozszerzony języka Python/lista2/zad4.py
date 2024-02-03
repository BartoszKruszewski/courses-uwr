from random import randint
from text_downloader import download_text

def simplify_text(text, max_len, max_words):
    words = text.replace(',','').split(' ')
    words = list(filter(lambda word: len(word) <= max_len, words))
    while len(words) > max_words:
        words.pop(randint(0, len(words) - 1))
    return " ".join(words)

url = 'https://pl.wikisource.org/wiki/Romeo_i_Julia_' \
'(Shakespeare,_t%C5%82um._Ho%C5%82owi%C5%84ski,_1839)/Akt_I'

print(simplify_text(download_text(url), 6, 20))