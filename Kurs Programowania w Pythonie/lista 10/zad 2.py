def caesar(s, k):
    alphabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
    result = ""
    for a in s:
        for i, b in enumerate(alphabet):
            if a == b:
                result += alphabet[(i + k) % 32]
    return result

data = sorted([x.rstrip() for x in open("slowa.txt","r",encoding="utf8").readlines()], key=lambda x: len(x), reverse=True)
words_len = {}
for word in data:
    l = len(word)
    if l in words_len:
        words_len[l].append(word)
    else:
        words_len[l] = [word]

for word in data:
    for k in range(1,32):
        if caesar(word,k) in words_len[len(word)]:
            print(word)
            break



