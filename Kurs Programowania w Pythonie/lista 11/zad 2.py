def pnf(word):
    assignments = {}
    i = 1
    for letter in word:
        if not letter in assignments:
            assignments[letter] = i
            i += 1
    result = ""
    for letter in word:
        result += str(assignments[letter]) + "-"
    return result[:-1]

print(pnf("tak"))
print(pnf("nie"))
print(pnf("indianin"))
