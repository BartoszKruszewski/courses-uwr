def minimum(n, tab):
    if n == 1:
        return tab[0]
    else:
        tab1 = [0] * (n // 2 + n % 2)
        tab2 = [0] * (n // 2)

        for i in range(n // 2):
            tab1[i] = tab[i]
            tab2[i] = tab[i + n // 2]

        if n % 2 == 1:
            tab1[n // 2] = tab[n // 2]

        min1 = minimum(n // 2 + n % 2, tab1)
        min2 = minimum(n // 2, tab2)

        if min1 <= min2:
            return min1
        else:
            return min2


print(minimum(10, [10, 45, 6, 1, 5, 6, 5, 4, 3, 6]))
