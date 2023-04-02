def get_pnf(word):
    assignments = {}
    i = 1
    for letter in word:
        if letter not in assignments:
            assignments[letter] = i
            i += 1
    result = ""
    for letter in word:
        result += str(assignments[letter]) + "-"
    return result[:-1]


def is_potencial_word(pnf, template):
    pnf_letters = pnf.split("-")
    template_letters = template.split("-")
    for i in range(len(pnf_letters)):
        occurrences_pnf = []
        for index, j in enumerate(pnf_letters):
            if pnf_letters[i] == j:
                occurrences_pnf.append(index)
        occurrences_template = []
        for index, j in enumerate(template_letters):
            if template_letters[i] == j:
                occurrences_template.append(index)
        if occurrences_template != occurrences_pnf:
            return False
    return True


def decode(text):
    ALPHABET = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
    words = text.split(" ")
    acceptable_words = [line.rstrip() for line in open("popularne_slowa.txt", "r", encoding="utf8").readlines()]
    result = []
    for word in words:
        if word not in [".", ",", "?"]:
            template = get_pnf(word)
            actual_length = len(word)
            same_length_words = [w for w in acceptable_words if len(w) == actual_length]
            same_pnf_words = [w for w in same_length_words if is_potencial_word(get_pnf(w), template)]
            print(same_pnf_words)

    return result


print(decode("udhufńfd ąuąuęąę yrrożdśś śdśsdtsć"))
