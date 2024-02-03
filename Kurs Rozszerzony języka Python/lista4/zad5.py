def combinations(n):
    if n == 0:
        yield () 
    else:
        for digit in range(10):
            for combo in combinations(n - 1):
                if digit not in combo:
                    yield digit, *combo

def word_to_number(word, assign):
    s = 0
    k = 1
    for digit in map(lambda l: assign[l], reversed(word)):
        s += digit * k
        k *= 10
    return s

def solve(word1, word2, word3, operator):
    letters = set(word1) | set(word2) | set(word3)
    for comb in combinations(len(letters)):
        assign = {letter: number for letter, number in zip(letters, comb)}
        number1 = word_to_number(word1, assign)
        number2 = word_to_number(word2, assign)
        number3 = word_to_number(word3, assign)
        if operator(number1, number2) == number3:
            return f'{number1} o {number2} = {number3} {assign}'
    return False
            
print(solve('KIOTO', 'OSAKA', 'TOKIO', lambda x, y: x + y))

