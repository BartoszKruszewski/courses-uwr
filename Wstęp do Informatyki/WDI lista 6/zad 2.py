def selection_sort(tab,n):
    for i in range(n):
        m = tab[i]
        index = i
        for j in range(n - i):
            p = j + i
            if tab[p] < m:
                m = tab[p]
                index = p
        tab[index] = tab[i]
        tab[i] = m
    return tab

tab = [5,7,3,4,5,3,4,67,5,3,34,6,6,4,6,67,6,5,5,5]
print(selection_sort(tab,len(tab)))

