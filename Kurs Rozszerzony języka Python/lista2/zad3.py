from text_downloader import download_text


def get_language_stats(text):
    LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    stats = {letter : 0 for letter in LETTERS}
    all_letters_count = 0

    for ch in text.lower():
        # zliczanie wszystkich znakow bedacych dozwolonymi literami
        if ch in LETTERS:
            stats[ch] += 1
            all_letters_count += 1

    # zwrocenie statystyk z procentowym udzialem kazdej litery w jezyku
    return {letter : round(amount / all_letters_count, 3) for (letter, amount) in stats.items()}


def get_language(text, language_stats):

    # utworzenie danych statycznych o tekscie
    text_stats = get_language_stats(text)

    # liczenie roznic pomiedzy statystykami tekstu a wszystkimi jezykami
    differences = {language:0 for language in language_stats.keys()}
    for (language, stats) in language_stats.items():
        for (amount1, amount2)  in zip(stats.values(), text_stats.values()):
            differences[language] += abs(amount1 - amount2)

    # wypisanie roznic
    print({language : round(difference, 3) for (language, difference) in differences.items()})

    # zwrocenie najmniej rozniacego sie jezyka
    return min(differences, key=lambda key: differences[key])


# wygenerowanie danych statystycznych o poszczegolnych jezykach

text_polish = open('ballady_i_romanse.txt', 'r', encoding='UTF-8').read()
text_english = open('alice_in_wonderland.txt', 'r', encoding='UTF-8').read()
text_german = open('faust.txt', 'r', encoding='UTF-8').read()

polish_stats = get_language_stats(text_polish)
english_stats = get_language_stats(text_english)
german_stats = get_language_stats(text_german)

language_stats = {
    'polish': polish_stats,
    'english': english_stats,
    'german': german_stats
}

# testy

url_polish = 'https://pl.wikipedia.org/wiki/Python'
url_english = 'https://en.wikipedia.org/wiki/Python'
url_german = 'https://de.wikipedia.org/wiki/Python'

print(get_language(download_text(url_polish), language_stats))
print(get_language(download_text(url_english), language_stats))
print(get_language(download_text(url_german), language_stats))
