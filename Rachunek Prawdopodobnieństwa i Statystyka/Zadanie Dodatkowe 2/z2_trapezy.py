# Bartosz Kruszewski
# 26.04.2024
# Wyznaczanie wartości dystrybuanty rozkładu normalnego

from math import sqrt, pi, e

def cdf(u: float, v: float, x: float, n: int = 1000000) -> float:
    '''Funkcja obliczająca wartość dystrybuanty rozkładu normalnego.

    - u: wartość oczekiwana
    - v: odchylenie standardowe
    - x: argument dystrybuanty
    - n: liczba węzłów

    Funkcja wykorzystuje złożoną metodę trapezów.
    '''

    # mozemy obliczyć wcześniej
    a = (x - u) / sqrt(2) / v 

    # dwa pierwsze wyrazy dzielimy przez 2
    s = (e ** -(-1 * a) ** 2 + e ** -((-1 + 2 / n) * a) ** 2) / 2 

    # sumowanie kolejnych wyrazów sumy
    s += sum(e ** -(t / n * a) ** 2 for t in range(-n + 4, n + 1, 2))

    # obliczanie koncowego wyniku
    return (1 + (x - u) / sqrt(2 * pi) / v * 2 / n  * s) / 2

# testy
if __name__ == '__main__':
    print('\n')
    print(f'    Test    |        Wyniki         |      WolframAlpha    ')
    print(f'------------|-----------------------|----------------------')
    print(f'0.0 1.0 0.5 | {cdf(0.0, 1.0, 0.5):.19f} | 0.6914624612740131036')
    print(f'2.0 1.7 0.3 | {cdf(2.0, 1.7, 0.3):.19f} | 0.1586552539314570514')
    print(f'1.1 1.2 0.9 | {cdf(1.1, 1.2, 0.9):.19f} | 0.4338161673890963463')
    print(f'0.1 0.2 0.4 | {cdf(0.1, 0.2, 0.4):.19f} | 0.9331927987311419339')
    print(f'8.0 5.4 0.6 | {cdf(8.0, 5.4, 0.6):.19f} | 0.0852856581920806146')
    print('\n')