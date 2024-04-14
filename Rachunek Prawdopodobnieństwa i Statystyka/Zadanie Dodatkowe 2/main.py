import math

def erf(x):
    '''Funkcja obliczajaca erf(x) uzywajac kwadratury Gaussa-Legeandre'a.

    Funkcja uzywa 10 wezlow.
    '''

    nodes = [
        0.14887433898163122, 0.4333953941292472, 0.6794095682990244, 0.8650633666889845,
        0.9739065285171717, -0.14887433898163122, -0.4333953941292472, -0.6794095682990244, 
        -0.8650633666889845, -0.9739065285171717
    ]
    
    weights = [
        0.2955242247147529, 0.2692667193099963, 0.2190863625159820, 0.1494513491505806, 
        0.0666713443086881, 0.2955242247147529, 0.2692667193099963, 0.2190863625159820, 
        0.1494513491505806, 0.0666713443086881
    ]
    
    result = 0
    for i in range(10):
        xi = (x * nodes[i] + x) / 2  # Zamiana przedzialu z (-1, 1) na (0, x)
        result += weights[i] * math.exp(-xi**2)

    return 1 / math.sqrt(math.pi) * result * x

def cdf(expected_value, standard_deviation, x):
    return (1 + erf((x - expected_value) / (standard_deviation * math.sqrt(2)))) / 2

print(cdf(2, 4, 0.5))
0.6914624612740617
