def ceasar(s, k):
    alphabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
    result = ""
    for a in s:
        for i, b in enumerate(alphabet):
            if a == b:
                result += alphabet[(i + k) % 32]
    return result


print(ceasar("cesarskim", 13))
