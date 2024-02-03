from math import sqrt
from random import randint

TARGET_SIZE = 100000
TARGET_CENTER = TARGET_SIZE / 2
PRECISION = 10000

ltwo = 0
cltwt = 0

for i in range(PRECISION):

    # losowanie pozycji
    x = randint(0, TARGET_SIZE)
    y = randint(0, TARGET_SIZE)

    # sprawdzanie, czy wylosowano pozycje wewnatrz okregu
    if sqrt((x - TARGET_CENTER) ** 2 + (y - TARGET_CENTER) ** 2) <= TARGET_CENTER:
        ltwo += 1
    cltwt += 1

    print(4 * ltwo / cltwt)
