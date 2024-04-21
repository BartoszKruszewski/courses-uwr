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

print(cdf(0, 1, 2.21))
