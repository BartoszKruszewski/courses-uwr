# Bartosz Kruszewski
# zad 1 lista 1 z PO: figury
# Python 3.11

# W Pythonie nie ma "struct", więc w tym programie zasymulowałem go za pomocą "class" bez użycia metod.
# Python nie jest dobrze przystosowany do takiego rozwiązanie co skutkuje koniecznością użcyia __new__() podczas
# deklarowania nowej "struktury".

class Figure:
    type = ""
    x = 0
    y = 0
    size = 0

def new_square(x, y, size):
    if size < 0:
        print("Dlugość boku kwadratu nie może być ujemna!")
    else:
        f = Figure.__new__(Figure) # wcześniej wspomniane deklarowanie nowej struktury
        f.type = "square"
        f.x = x
        f.y = y
        f.size = size
        return f

def new_circle(x, y, size):
    if size < 0:
        print("Promień koła nie może być ujemny!")
    else:
        f = Figure.__new__(Figure) # wcześniej wspomniane deklarowanie nowej struktury
        f.type = "circle"
        f.x = x
        f.y = y
        f.size = size
        return f

def new_triangle(x, y, size):
    if size < 0:
        print("Dlugość boku trójkąta nie może być ujemna!")
    else:
        f = Figure.__new__(Figure) # wcześniej wspomniane deklarowanie nowej struktury
        f.type = "triangle"
        f.x = x
        f.y = y
        f.size = size
        return f

def area(f):
    if f.type == "square":
        return f.size * f.size
    elif f.type == "circle":
        return 3.14 * f.size * f.size # przybliżenie pi jako 3.12
    elif f.type == "triangle":
        return 0.43 * f.size * f.size # przybliżenie sqrt(3)/2 jako 0.43

def move(f, x, y):
    f.x += x
    f.y += y

def show(f):
    print(f.type, f.x, f.y)

def sum_of_areas(F):
    sum = 0
    for f in F:
        sum += area(f)
    return sum

