import math

def z2(u, v, x, max_iter = 20):
    '''Funkcja obliczająca wartość dystrybuanty rozkładu normalnego.

    - u: wartość oczekiwana
    - v: odchylenie standardowe
    - x: argument dystrybuanty
    - n: liczba węzłów

    Funkcja wykorzystuje złożoną metodę trapezów.
    '''

    # utworzenie oszczędnej tablicy Romberga
    # (utrzymujemy jednocześnie tylko jedną kolumnę)
    R = [0] * max_iter

    # wypełnienie pierwszej kolumny z pomocą wzoru trapezów
    for k in range(max_iter):

        # mozemy obliczyć wcześniej
        n = 2 ** k
        a = (x - u) / math.sqrt(2) / v 

        # dwa pierwsze wyrazy dzielimy przez 2
        s = (math.e ** -(-1 * a) ** 2 + math.e ** -((-1 + 2 / n) * a) ** 2) / 2 

        # sumowanie kolejnych wyrazów sumy
        s += sum(math.e ** -(t / n * a) ** 2 for t in range(-n + 4, n + 1, 2))

        # obliczanie koncowego wyniku
        R[k] = (1 + (x - u) / math.sqrt(2 * math.pi) / v * 2 / n  * s) / 2

    # wypełnienie pozostałych kolumn
    p1 = R[0]
    p2 = R[1]
    for k in range(1, max_iter):
        for j in range(1, k + 1):
            p2 = p1
            p1 = R[k]
            R[k] = (4 ** j * p1 - p2) / (4 ** j - 1)
    
    # odczytanie wyniku z ostatniej kolumny
    return R[max_iter - 1]

print(z2(5, 4, 2))
