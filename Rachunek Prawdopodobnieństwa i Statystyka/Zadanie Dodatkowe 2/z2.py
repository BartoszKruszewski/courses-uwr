# Bartosz Kruszewski
# 15.04.2024
# Wyznaczanie wartości dystrybuanty rozkładu normalnego

from math import sqrt, pi, e

def cdf(u: float, v: float, x: float) -> float:
    '''Funkcja obliczająca wartość dystrybuanty rozkładu normalnego.

    - u: wartość oczekiwana
    - v: odchylenie standardowe
    - x: argument dystrybuanty

    Funkcja wykorzystuje kwadraturę Gaussa-Legendre'a z 10 węzłami.
    '''
    
    # węzły
    t = [
        0.14887433898163122, 0.4333953941292472, 0.6794095682990244,
        0.8650633666889845, 0.9739065285171717, -0.14887433898163122, 
        -0.4333953941292472, -0.6794095682990244, -0.8650633666889845, 
        -0.9739065285171717
    ]
    
    # wagi
    w = [
        0.2955242247147529, 0.2692667193099963, 0.2190863625159820, 
        0.1494513491505806, 0.0666713443086881, 0.2955242247147529,
        0.2692667193099963, 0.2190863625159820, 0.1494513491505806,
        0.0666713443086881
    ]

    a = (x - u) / sqrt(2) / v # mozemy obliczyć wcześniej
    s = sum(w[i] * e ** (-1 * (t[i] * a) ** 2) for i in range(10))
    return (1 + (x - u) / sqrt(2 * pi) / v * s) / 2

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
