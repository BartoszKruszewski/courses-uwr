L = [1, 2, 3, 1, 2, 3, 8, 2, 2, 2, 9, 9, 4]


def usun_duplikaty(lista):
    for i, n in enumerate(lista):
        lista[i] = (n, i)

    lista.sort(key=lambda x: x[0])

    i = 0
    while i < len(lista) - 1:

        if lista[i][0] == lista[i + 1][0]:
            lista.pop(i + 1)
        else:
            i += 1

    lista.sort(key=lambda x: x[1])

    for i in range(len(lista)):
        lista[i] = lista[i][0]


usun_duplikaty(L)
print(L)
