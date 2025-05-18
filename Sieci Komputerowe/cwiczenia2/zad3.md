Sume kontrolą obliczamy używając wzoru:

$CRC = {M(x)\ \cdot x^r} \mod {G(x)}$

gdzie:

$M(x)$ to wiadomość

mnożenie przez $x^r$ to uzupełnienie zerami do odpowiedniego stopnia

$G(x)$ to wielomian, którego używa algorytm

Dzielenie z resztą jest wykonywane w pierścieniu wielomianów $F_2$

Sume kontrolą doklejamy do wiadomości.

|               | $G(x) = x^2 + x + 1 = 111$ | $G(x) = x^7 + 1 = 10000001$ |
| ------------- | -------------------------- | --------------------------- |
| Dopisanie zer | 1010**00**                 | 1010**0000000**             |
| CRC           | 10                         | 0001010                     |
| Ramka         | 1010**10**                 | 1010**0001010**             | 
