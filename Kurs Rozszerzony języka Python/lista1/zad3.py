def table(x1, x2, y1, y2, d):
    # wyznaczanie poziomych etykiet
    lx = []
    n = x1
    while n < x2:
        lx.append(n)
        n += d
    lx.append(x2)

    # wyznaczanie pionowych etykiet
    ly = []
    n = y1
    while n < y2:
        ly.append(n)
        n += d
    ly.append(y2)

    # wyznaczanie szerokosci kolumn
    all_numbers = []
    all_numbers.extend(lx)
    all_numbers.extend(ly)
    for x in lx:
        for y in ly:
            all_numbers.append(x * y)
    col_width = max(map(get_length, all_numbers))
    first_col_width = max(map(get_length, ly))

    # rysowanie poziomych etykiet
    print(" " * first_col_width, end=" ")
    for x in lx:
        same_width_print(x, col_width)
    print()

    # rysowanie liczb na przecieciach kolumn i wierszy
    for y in ly:

        # rysowanie pionowych etykiet
        same_width_print(y, first_col_width)
        for x in lx:
            same_width_print(x * y, col_width)
        print()


def get_length(number):
    return len(str(number))


def same_width_print(number, width):
    print((width - get_length(number) + 1) * " ", number, sep="", end="")


table(3.0, 5.0, 2.0, 4.0, 1.0)
