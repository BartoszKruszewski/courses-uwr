from math import ceil

a = 230
b = 132216

while a != 0:
    x = ceil(b / a)
    print(f'1/{x}', a)
    a *= x
    a -= b
    b *= x