import random


def randinf(k):
    y = 1 - random.random()
    z = k * (1 / y - 1)
    return int(z)


def better_split(ex):
    result = []
    actual_ex = ""
    l = 0
    for i in ex:
        if i == "(":
            l += 1
        elif i == ")":
            l -= 1
        elif i == "+":
            if l == 0:
                if actual_ex[0] == "+":
                    actual_ex = actual_ex[1:]
                result.append(actual_ex)
                actual_ex = ""
        actual_ex += i
    if actual_ex != "":
        if actual_ex[0] == "+":
            actual_ex = actual_ex[1:]
        result.append(actual_ex)
    return result


def regex(ex):
    expression = random.choice(better_split(ex))
    print(expression)
    result = ""
    i = 0
    while i < len(expression) and expression[i] != "(":
        result += expression[i]
        i += 1
    rest = expression[i + 1:-2]
    if rest != "":
        result += regex(rest) * (randinf(2) + 1)

    return result


print(regex("abc+bc(dab(cc)*)*+(a+b)*"))