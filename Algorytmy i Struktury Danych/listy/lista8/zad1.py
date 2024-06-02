def optimal_bst(p, n):

    # minimalny koszt dla przedzialu i:j
    e = [[float('inf') for _ in range(n)] for _ in range(n)]

    # suma prawdopodobienstw dla przedzialu i:j
    w = [[0 for _ in range(n)] for _ in range(n)]
    
    # tablica do odzyskiwania
    # pamięta jaki wierzcholek jest korzeniem dla danego przedzialu
    root = [[0 for _ in range(n)] for _ in range(n)]

    # przypisanie wartości początkowych
    for i in range(n):
        w[i][i] = p[i]
        e[i][i] = p[i]
        root[i][i] = i
    
    # iteracja po długości poddrzewa
    for l in range(2, n + 1):

        # iteracja po indeksie początkowym przedzialu
        for i in range(n - l + 1):

            # obliczenie indeksu koncowego przedzialu
            j = i + l - 1

            # zaktualizowanie sumy prawdopodobienstw
            w[i][j] = w[i][j - 1] + p[j]

            # iteracja po korzeniach
            for r in range(i, j + 1):

                # zaktualizowanie kosztu
                cost = e[i][r - 1] + e[r + 1][j] + w[i][j]
                e[i][j] = min(e[i][j], cost)

                # zapamietanie korzenia dla przedzialu
                root[i][j] = r

    return e, root

# odzyskiwanie drzewa
def build_tree(root, keys, i, j):

    # jeżeli przedział jest błedy to zwróc pusty wskaznik
    if i > j:
        return None
    
    # tworzenie drzewa rekurencyjnie
    node = {
        'key': keys[root[i][j]],
        'left': build_tree(root, keys, i, root[i][j] - 1),
        'right': build_tree(root, keys, root[i][j] + 1, j)
    }

    return node

# Złożoność: O(n3), bo trzy pętle w pętli

# Poprawność:
# Koszt obliczamy jako: suma(wysokość wierzchołka * ppb wierzchołka)
# Zauważmy, że koszt[i:j] = koszt[i:korzeń] + koszt[korzeń:j] + suma_ppb[i:j]
# Znając to własnośc oraz sumy ppb przedziałów, mamy klasycznego dynamika,
# z tym, że musimy najpierw obliczyć krótsze przedziały, żeby móc obliczyć dłuższe.
# Stąd iteracja po długościach przedziału.
# Jakby narysować przedziały po jakich iteruje, to idziemy po poddrzewach, od liści do pełnego drzewa.

